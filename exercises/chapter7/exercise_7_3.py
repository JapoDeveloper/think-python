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
