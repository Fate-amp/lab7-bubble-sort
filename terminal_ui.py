"""Terminal renderer for bubble sort visualization.

This module only draws frames; it does not implement sorting logic.
It consumes SortStep objects from sorting_logic.bubble_sort_steps.
"""

import os
import time

from sorting_logic import SortStep, bubble_sort_steps


def _bar_for_value(value: int) -> str:
    """Map a numeric value to a horizontal ASCII bar."""
    return "#" * max(0, int(value))


def _clear_terminal() -> None:
    """Clear terminal in a cross-platform way."""
    os.system("cls" if os.name == "nt" else "clear")


def draw_terminal_frame(step: SortStep, delay: float = 0.25) -> None:
    """Render one terminal frame from a SortStep.

    The frame contains:
    1. Metadata header (pass, compare index, action).
    2. One row per value as index | bar.
    3. A caret marker on the left compared row.
    """
    _clear_terminal()
    print(
        f"Pass: {step.pass_index} | Comparing index: {step.compare_index} | "
        f"Action: {step.action} | Swapped this step: {step.swapped_this_step}"
    )
    print(f"Unsorted end index: {step.end_index}")

    # Draw each row as "index | ####".
    for index, value in enumerate(step.values):
        bar = _bar_for_value(value)
        print(f"{index} | {bar}")

        # Show marker at the left compare index (j).
        if step.compare_index is not None and index == step.compare_index:
            print("    ^")

    time.sleep(delay)


def visualize_bubble_sort_terminal(arr: list[int], delay: float = 0.25) -> list[int]:
    """Play all sort frames in terminal and return final sorted values."""
    original = arr.copy()
    last_values = arr.copy()

    # Step stream comes from logic module; terminal module only renders.
    for step in bubble_sort_steps(arr):
        last_values = step.values
        draw_terminal_frame(step, delay)

    print(f"Original: {original}")
    print(f"Sorted:   {last_values}")
    return last_values
