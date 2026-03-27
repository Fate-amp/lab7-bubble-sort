"""
Bubble Sort Implementation
A simple sorting algorithm that repeatedly steps through the list, 
compares adjacent elements, and swaps them if they're in the wrong order.
"""

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
        swapped=False
        # TODO: Create the inner loop that compares adjacent elements
        # Each pass should compare: arr[0] with arr[1], arr[1] with arr[2], etc.
        for j in range(len(arr) - 1 - i):
            
            # TODO: Compare arr[j] with arr[j+1]
            # If arr[j] is greater than arr[j+1], we need to swap them
            # (Uncomment and fill in the condition below)
            # if ???:
            #     TODO: Swap arr[j] and arr[j+1]
            #     You can use tuple unpacking: arr[j], arr[j+1] = arr[j+1], arr[j]
            
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
        if not swapped:
            return arr
    # TODO: Return the sorted array
    return arr


def _cell_row(values, width=4):
    """Return a fixed-width row so each frame stays aligned."""
    # TODO: Format each value to a fixed width and join into one row string.
    # TODO: Consider dynamic width based on largest absolute value.
    row = [f"{value:>{width}}" for value in values]
    return " ".join(row)


def _build_marker_row(length, marker_index=None, width=4):
    """Build marker row that points to compared indices with '^'."""
    # TODO: Create a marker list of size 'length'.
    # TODO: Put '^' under left_index and right_index, blank elsewhere.
    # TODO: Return aligned marker row string.
    markers = []

    for i in range(length):
        if i == marker_index:
            markers.append(f"{'^':>{width}}")
        else:
            markers.append(" " * width)        

    return " ".join(markers)


def _draw_frame(arr, pass_index, compare_index, end_index, action, delay=0.25):
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
    # TODO 1: Clear terminal in-place (ANSI) for animation effect.
    # TODO 2: Print header with pass index, compare index, and swapped/action info.
    # TODO 3: For each array element, print one line in format: "index | ####".
    # TODO 4: Print caret marker line for current compare index.
    # TODO 5: Pause using delay.
    print("\033[H\033[J", end="")
    print(f"Pass: {pass_index} | Comparing indices: {compare_index} | Swapped: {action}")

    for index, value in enumerate(arr):
        bar = "#" * max(0, int(value))
        print(f"{index} | {bar}")

        # Mark the left compared row, matching the screenshot-style behavior.
        if compare_index is not None and index == compare_index:
            print("^")

    time.sleep(delay)


def bubble_sort_visual(arr, delay=0.25):
    """
    Screenshot-style bubble sort visualization scaffold.

    This is a learning scaffold and intentionally leaves rendering logic open.
    """
    values = arr.copy()

    # TODO 1: Keep a copy of original values for final print.
    # TODO 2: Handle edge cases (empty list or single item).
    # TODO 3: Loop over bubble-sort passes.
    # TODO 4: In each compare step, compute swapped = True/False.
    # TODO 5: Call _draw_frame with screenshot-style metadata.
    # TODO 6: After sorting, print:
    #         Original: [...]
    #         Sorted:   [...]
    original = values.copy()

    if len(values) <= 1:
        _draw_frame(values, 0, 0 if values else None, 0, False, delay)
        print(f"Original: {original}")
        print(f"Sorted:   {values}")
        return values

    for i in range(len(values)):
        swapped = False
        end_index = len(values) - 1 - i

        for j in range(end_index):
            if values[j] > values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]
                swapped = True

            _draw_frame(values, i + 1, j, end_index, swapped, delay)

        if not swapped:
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