"""
Think Python, 2nd Edition
Chapter 6
Exercise 6.5

Description: 
The greatest common divisor (GCD) of a and b is the largest number that divides 
both of them with no remainder.

One way to find the GCD of two numbers is based on the observation that if r is 
the remainder when a is divided by b, then gcd(a,b) = gcd(b,r). As a base case, 
we can use gcd(a,0) = a.

Write a function called gcd that takes parameters a and b and returns their 
greatest common divisor.
"""


def gcd(a, b):
    """Calculate the greatest common divisor between integers 'a' and 'b'."""
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

print(gcd(2,3))   # 1
print(gcd(2,4))   # 2
print(gcd(9, 30)) # 3
print(gcd(8,12))  # 4
