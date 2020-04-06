"""
Think Python, 2nd Edition
Chapter 6
Exercise 6.4

Description: 
A number, a, is a power of b if it is divisible by b and a/b is a power of b. 
Write a function called is_power that takes parameters a and b and returns True 
if a is a power of b. Note: you will have to think about the base case.
"""


def is_power(a, b):
    """Check if a integer 'a' is a power of a integer 'b'"""
    if a == 1 or a == b: # base case
        return True
    elif a % b != 0:
        return False
    else:
        return is_power(a / b, b)

print(is_power(2,2)) # True
print(is_power(1,2)) # True
print(is_power(8,2)) # True
print(is_power(9,2)) # False