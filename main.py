"""Application entrypoint.

Responsibilities here are intentionally small:
1. Run simple non-visual examples.
2. Choose which UI demo to launch.
3. Keep algorithm/UI implementation details in dedicated modules.
"""

from pygame_ui import visualize_bubble_sort_pygame
from sorting_logic import bubble_sort
from terminal_ui import visualize_bubble_sort_terminal


def run_sort_examples() -> None:
    """Run non-visual examples to verify algorithm behavior quickly."""
    examples = [
        [64, 34, 25, 12, 22, 11, 90],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [42],
        [],
    ]

    for idx, values in enumerate(examples, start=1):
        result = bubble_sort(values)
        print(f"Example {idx} original: {values}")
        print(f"Example {idx} sorted:   {result}")
        print()


def main() -> None:
    """Entrypoint for demos.

Switch between terminal and pygame visualization by toggling the demo calls.
"""
    run_sort_examples()

    visual_input = [14, 1, 7, 13, 12, 2, 8, 10, 6, 5, 0, 3, 11, 9, 4]

    # Terminal visualization demo (text mode):
    # visualize_bubble_sort_terminal(visual_input, delay=0.15)

    # Pygame visualization demo (window mode):
    visualize_bubble_sort_pygame(visual_input, fps=20)


if __name__ == "__main__":
    main()
