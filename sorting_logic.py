"""Pure sorting logic with no UI concerns.

This module owns:
1. The bubble sort algorithm itself.
2. A step stream used by any UI (terminal or pygame) to render progress.
"""

from dataclasses import dataclass
from typing import Iterator, Optional


@dataclass(frozen=True)
class SortStep:
    """One visualization snapshot emitted by bubble_sort_steps.

    - values: current array state at this moment.
    - pass_index: current bubble sort pass (1-based for non-trivial arrays).
    - compare_index: left index j currently compared with j + 1.
    - end_index: right boundary of the unsorted section.
    - action: human-readable action label (No swap / Swapped / Sorted / Trivial).
    - swapped_this_step: whether current compare caused a swap.
    """

    values: list[int]
    pass_index: int
    compare_index: Optional[int]
    end_index: int
    action: str
    swapped_this_step: bool


def bubble_sort(arr: list[int]) -> list[int]:
    """Return a sorted copy of arr using bubble sort.

    Steps:
    1. Walk the unsorted section left to right.
    2. Swap adjacent out-of-order values.
    3. Shrink unsorted section after each pass.
    4. Stop early if no swap occurred in a full pass.
    """
    values = arr.copy()
    n = len(values)

    for i in range(n):
        swapped = False
        for j in range(0, n - 1 - i):
            if values[j] > values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]
                swapped = True

        if not swapped:
            break

    return values


def bubble_sort_steps(arr: list[int]) -> Iterator[SortStep]:
    """Yield state transitions so UIs can visualize bubble sort.

    This generator is intentionally UI-agnostic: it provides data only.
    Any renderer can consume these steps and draw them however it wants.
    """
    values = arr.copy()
    n = len(values)

    # Trivial case: emit exactly one frame so UIs can still render something.
    if n <= 1:
        yield SortStep(values.copy(), 0, None, 0, "Trivial", False)
        return

    for i in range(n):
        swapped_in_pass = False
        end_index = n - 1 - i

        # Compare each adjacent pair inside the current unsorted range.
        for j in range(end_index):
            swapped_this_step = False
            action = "No swap"

            if values[j] > values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]
                swapped_this_step = True
                swapped_in_pass = True
                action = "Swapped"

            # Emit frame after applying this compare step result.
            yield SortStep(
                values=values.copy(),
                pass_index=i + 1,
                compare_index=j,
                end_index=end_index,
                action=action,
                swapped_this_step=swapped_this_step,
            )

        # Early exit when a full pass made no changes.
        if not swapped_in_pass:
            break

    # Final frame to indicate completion.
    yield SortStep(values.copy(), n, None, 0, "Sorted", False)
