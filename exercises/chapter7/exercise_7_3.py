"""
Think Python, 2nd Edition
Chapter 7
Exercise 7.3

Description: 

The mathematician Srinivasa Ramanujan found an infinite series that can be used 
to generate a numerical approximation of 1/π:

    https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.pinimg.com%2Foriginals%2Fa1%2Ff5%2F81%2Fa1f581c7dc6c3c581a03902c15327ccb.jpg&f=1&nofb=1

Write a function called estimate_pi that uses this formula to compute and 
return an estimate of π. It should use a while loop to compute terms of the 
summation until the last term is smaller than 1e-15 
(which is Python notation for 10**-15). 
You can check the result by comparing it to math.pi.
"""

import math


def factorial(n):
    """calculate the factorial of a non-negative integer number"""
    if type(n) is not int or n < 0:
        print('Only non-negative integers are accepted.')
        return
    if n == 0:
        return 1
    return n * factorial(n-1)


def estimate_pi():
    """compute an approximation of pi"""
    k = 0
    total = 0
    epsilon = 1e-15
    factor = 2 * math.sqrt(2) / 9801
    while True:
        term = factor * (factorial(4*k) * (1103 + 26390 * k)
                         ) / (factorial(k)**4 * 396**(4*k))
        total += term
        if term < epsilon:
            break
        k += 1
    return 1 / total


print('Estimation of pi    :', estimate_pi())
print('Math module pi value:', math.pi)
