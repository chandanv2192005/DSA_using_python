"""
09_bubble_sort.py
Logic: Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order.
The pass through the list is repeated until the list is sorted.
"""

def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Flag to optimize: if no two elements were swapped by inner loop, then break
        swapped = False
        
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no two elements were swapped by inner loop, then break
        if not swapped:
            break
            
    return arr

# Test case
my_list = [64, 34, 25, 12, 22, 11, 90]
print(f"Original list: {my_list}")
sorted_list = bubble_sort(my_list.copy())
print(f"Sorted list:   {sorted_list}")
