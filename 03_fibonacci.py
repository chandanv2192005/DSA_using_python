"""
03_fibonacci.py
Logic: The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1.
Example: 0, 1, 1, 2, 3, 5, 8, 13, ...
"""

def generate_fibonacci(n_terms):
    if n_terms <= 0:
        return []
    elif n_terms == 1:
        return [0]
    
    sequence = [0, 1]
    while len(sequence) < n_terms:
        next_val = sequence[-1] + sequence[-2]
        sequence.append(next_val)
    return sequence

# Test case
terms = 10
print(f"Fibonacci sequence up to {terms} terms: {generate_fibonacci(terms)}")
