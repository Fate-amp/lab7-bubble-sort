"""
Bubble Sort Implementation
A simple sorting algorithm that repeatedly steps through the list, 
compares adjacent elements, and swaps them if they're in the wrong order.
"""

import os
import time


def bubble_sort(arr):
    """
    Sort an array using the bubble sort algorithm.
    
    Args:
        arr (list): A list of comparable elements to sort.
    
    Returns:
        list: The sorted array in ascending order.
    
    TODO: Implement the bubble sort logic below.
    Hint: You'll need an outer loop that controls how many passes you make,
    and an inner loop that compares adjacent elements.
    """
    
    # TODO: Create the outer loop that runs through the array multiple times
    # This loop should continue until the array is sorted (no swaps occur in a pass)
    for i in range(len(arr)):
        
        # TODO: Track whether any swap occurred in this pass
        # If no swaps occur, the array is already sorted and we can return early
        swapped = False
        # TODO: Create the inner loop that compares adjacent elements
        # Each pass should compare: arr[0] with arr[1], arr[1] with arr[2], etc.
        for j in range(len(arr) - 1 - i):
            
            # TODO: Compare arr[j] with arr[j+1]
            # If arr[j] is greater than arr[j+1], we need to swap them
            # (Uncomment and fill in the condition below)
            # if ???:
            #     TODO: Swap arr[j] and arr[j+1]
            #     You can use tuple unpacking: arr[j], arr[j+1] = arr[j+1], arr[j]
            
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            return arr
    # TODO: Return the sorted array
    return arr


def _bar_for_value(value):
    """Convert one numeric value into a screenshot-style bar."""
    return "#" * max(0, int(value))


def _clear_terminal():
    """Clear terminal in a cross-platform way."""
    os.system("cls" if os.name == "nt" else "clear")


def _draw_frame(arr, pass_index, compare_index, end_index, action, swapped_this_step, delay=0.25):
    """
    Draw one screenshot-style frame for the sorting animation.

    TODO:
    - Match this style:
      Pass: 5 | Comparing indices: 3 | Swapped: False
      0 | 
      1 | ##
      2 | #####
      ...
      ^
    """
    _clear_terminal()
    print(
        f"Pass: {pass_index} | Comparing index: {compare_index} | "
        f"Action: {action} | Swapped this step: {swapped_this_step}"
    )
    print(f"Unsorted end index: {end_index}")

    for index, value in enumerate(arr):
        bar = _bar_for_value(value)
        print(f"{index} | {bar}")

        # Mark the left compared row, matching the screenshot-style behavior.
        if compare_index is not None and index == compare_index:
            print("    ^")

    time.sleep(delay)


def bubble_sort_visual(arr, delay=0.25):
    """
    Screenshot-style bubble sort visualization scaffold.

    This is a learning scaffold and intentionally leaves rendering logic open.
    """
    values = arr.copy()
    original = values.copy()

    if len(values) <= 1:
        _draw_frame(values, 0, 0 if values else None, 0, "Trivial", False, delay)
        print(f"Original: {original}")
        print(f"Sorted:   {values}")
        return values

    for i in range(len(values)):
        swapped_in_pass = False
        end_index = len(values) - 1 - i

        for j in range(end_index):
            action = "No swap"
            swapped_this_step = False
            if values[j] > values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]
                swapped_this_step = True
                swapped_in_pass = True
                action = "Swapped"

            _draw_frame(values, i + 1, j, end_index, action, swapped_this_step, delay)

        if not swapped_in_pass:
            break

    print(f"Original: {original}")
    print(f"Sorted:   {values}")
    return values


def main():
    """Test the bubble sort function with various test cases."""
    
    # Test case 1: Unsorted array
    test1 = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original array: {test1}")
    result1 = bubble_sort(test1)
    print(f"Sorted array: {result1}")
    print()
    
    # Test case 2: Already sorted array
    test2 = [1, 2, 3, 4, 5]
    print(f"Original array: {test2}")
    result2 = bubble_sort(test2)
    print(f"Sorted array: {result2}")
    print()
    
    # Test case 3: Reverse order array
    test3 = [5, 4, 3, 2, 1]
    print(f"Original array: {test3}")
    result3 = bubble_sort(test3)
    print(f"Sorted array: {result3}")
    print()
    
    # Test case 4: Single element
    test4 = [42]
    print(f"Original array: {test4}")
    result4 = bubble_sort(test4)
    print(f"Sorted array: {result4}")
    print()
    
    # Test case 5: Empty array
    test5 = []
    print(f"Original array: {test5}")
    result5 = bubble_sort(test5)
    print(f"Sorted array: {result5}")

    # Visualization demo scaffold (enable after implementing TODOs above).
    visual_input = [14, 1, 7, 13, 12, 2, 8, 10, 6, 5, 0, 3, 11, 9, 4]
    bubble_sort_visual(visual_input, delay=0.15)


if __name__ == "__main__":
    main()