"""
07_anagram_check.py
Logic: Two strings are anagrams if they contain the same characters in any order.
Example: 'listen' and 'silent'
"""

def are_anagrams(s1, s2):
    # Remove whitespace and convert to lowercase for uniform comparison
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    
    # Method 1: Sorting
    # return sorted(s1) == sorted(s2)
    
    # Method 2: Frequency counting (More efficient)
    if len(s1) != len(s2):
        return False
        
    counts = {}
    
    for char in s1:
        counts[char] = counts.get(char, 0) + 1
        
    for char in s2:
        if char not in counts:
            return False
        counts[char] -= 1
        if counts[char] < 0:
            return False
            
    return True

# Test cases
str1 = "Listen"
str2 = "Silent"
print(f"Are '{str1}' and '{str2}' anagrams? {are_anagrams(str1, str2)}")

str3 = "Hello"
str4 = "World"
print(f"Are '{str3}' and '{str4}' anagrams? {are_anagrams(str3, str4)}")
