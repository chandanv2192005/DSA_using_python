"""
10_binary_search.py
Logic: Binary Search is an efficient algorithm for finding an item from a sorted list of items. 
It works by repeatedly dividing in half the portion of the list that could contain the item, until you've narrowed down the possible locations to just one.
"""

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        # Check if target is present at mid
        if arr[mid] == target:
            return mid
        # If target is greater, ignore left half
        elif arr[mid] < target:
            low = mid + 1
        # If target is smaller, ignore right half
        else:
            high = mid - 1
            
    # If we reach here, then the element was not present
    return -1

# Test case
sorted_list = [2, 3, 4, 10, 40]
target = 10

result = binary_search(sorted_list, target)
print(f"List: {sorted_list}, Target: {target}")

if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in array")
