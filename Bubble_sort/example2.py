# Example 2: Sorting an array with negative numbers and duplicates

my_array2 = [45, 0, -11, 23, 11, -11, 0, 78]

print("Original array:", my_array2)

n = len(my_array2)
for i in range(n-1):
    swapped = False
    for j in range(n-i-1):
        if my_array2[j] > my_array2[j+1]:
            my_array2[j], my_array2[j+1] = my_array2[j+1], my_array2[j]
            swapped = True
    # If no swaps occurred during a full pass, the array is sorted
    if not swapped:
        print(f"Array sorted early after {i+1} passes.")
        break

print("Sorted array:", my_array2)
