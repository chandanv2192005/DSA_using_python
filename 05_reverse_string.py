"""
05_reverse_string.py
Logic: Reversing string order. 
Python provides several elegant ways to do this.
"""

def reverse_slicing(s):
    # Method 1: Slicing (Fastest and most Pythonic)
    return s[::-1]

def reverse_loop(s):
    # Method 2: Manual approach using a loop (Good for understanding logic)
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

def reverse_joined(s):
    # Method 3: Using reversed() and join()
    return "".join(reversed(s))

# Test cases
original = "Interview"
print(f"Original: {original}")
print(f"Reversed (Slicing): {reverse_slicing(original)}")
print(f"Reversed (Loop):    {reverse_loop(original)}")
print(f"Reversed (Joined):  {reverse_joined(original)}")
