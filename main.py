from typing import List
def bubble_sort(arr:List[int])->List[int]:
    end=len(arr)-1
    current=1
    while end>0:
        if current<end and arr[current]>arr[current-1]:
            arr[current-1],arr[current]=arr[current],arr[current-1]
        current+=1
    return arr

array=[8,-1,2,6,3]
bubble_sort(array)