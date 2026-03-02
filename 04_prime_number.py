"""
04_prime_number.py
Logic: A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
        
    # We only need to check divisors up to the square root of n
    # because if n has a factor larger than sqrt(n), it must also have a factor smaller than sqrt(n).
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

# Test cases
nums = [2, 15, 17, 23, 100]
for num in nums:
    print(f"Is {num} prime? {is_prime(num)}")
