"""
08_fizzbuzz.py
Logic: Print numbers from 1 to n. 
For multiples of 3 print "Fizz" instead of the number.
For multiples of 5 print "Buzz".
For numbers which are multiples of both 3 and 5 print "FizzBuzz".
"""

def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Test case
print("FizzBuzz output for 1 to 15:")
fizzbuzz(15)
