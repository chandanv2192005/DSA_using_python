# Example 3: Sorting strings alphabetically

words = ["banana", "apple", "cherry", "date", "elderberry"]

print("Original words:", words)

n = len(words)
for i in range(n-1):
    swapped = False
    for j in range(n-i-1):
        if words[j] > words[j+1]:
            # Python can compare strings based on lexicographical (alphabetical) order!
            words[j], words[j+1] = words[j+1], words[j]
            swapped = True
    if not swapped:
        break

print("Sorted words:", words)
