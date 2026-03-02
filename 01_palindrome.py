"""
01_palindrome.py
Logic: A palindrome is a string or number that reads the same forwards and backwards.
Example: 'racecar', 121
"""

def is_palindrome_string(s):
    # Method 1: Slicing (The Pythonic way)
    # s[::-1] creates a reversed copy of the string
    reversed_str = s[::-1]
    return s == reversed_str

def is_palindrome_number(n):
    # Method 2: Mathematical approach for numbers
    if n < 0:
        return False
    
    original = n
    reversed_num = 0
    
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
        
    return original == reversed_num
original_string = input("enter thr string ")
num_string = input("enter the number")
test_num = int(num_string)
# Test cases

print(f"Is '{original_string}' a palindrome? {is_palindrome_string(original_string)}")


print(f"Is {test_num} a palindrome? {is_palindrome_number(test_num)}")
