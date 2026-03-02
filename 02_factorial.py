"""
02_factorial.py
Logic: The factorial of a non-negative integer n is the product of all positive integers less than or equal to n.
Example: 5! = 5 * 4 * 3 * 2 * 1 = 120
"""

def factorial_recursive(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive step: n * (n-1)!
    return n * factorial_recursive(n - 1)

def factorial_iterative(n):
    result = 1
    factors = []
    for i in range(1, n + 1):
        result *= i
        factors.append(str(i))
    display_string = "*".join(factors)
    return result, display_string

# Test cases
num = 5
print(f"Factorial of {num} (Recursive): {factorial_recursive(num)}")
factorial_result, display_string = factorial_iterative(num)
print(f"Factorial of {display_string} = {factorial_result}") 