"""
06_second_largest.py
Logic: Find the second largest element in a list without using built-in sort() functions.
Example: [10, 20, 4, 45, 99] -> 45
"""

def find_second_largest(arr):
    if len(arr) < 2:
        return None
    
    # Initialize with negative infinity
    first = second = float('-inf')
    
    for num in arr:
        # If current number is greater than first, update both
        if num > first:
            second = first
            first = num
        # If current number is between first and second
        elif num > second and num != first:
            second = num
            
    return second if second != float('-inf') else None

# Test cases
my_list = [10, 20, 4, 45, 99]
print(f"List: {my_list}")
print(f"Second largest: {find_second_largest(my_list)}")

another_list = [10, 10, 8]
print(f"List: {another_list}")
print(f"Second largest: {find_second_largest(another_list)}")
