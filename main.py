"""
Bubble Sort Implementation
A simple sorting algorithm that repeatedly steps through the list, 
compares adjacent elements, and swaps them if they're in the wrong order.
"""


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
    
    # TODO: Return the sorted array
    return arr


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


if __name__ == "__main__":
    main()