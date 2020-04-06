"""
Think Python, 2nd Edition
Chapter 6
Exercise 6.2

Description: 

The Ackermann function, A(m,n), is defined:

         n + 1            if m = 0
A(m,n) = A(m-1, 1)        if m > 0 and n = 0
         A(m-1, A(m,n-1)) if m > 0 and n > 0

See http://en.wikipedia.org/wiki/Ackermann_function. 

Write a function named ack that evaluates the Ackermann function. 
Use your function to evaluate ack(3, 4), which should be 125. 
What happens for larger values of m and n?
"""


def ack(m, n):
    if m < 0 or n < 0:
        print('ack function called with invalid input, only positive integers are valid')
        return
    elif m == 0:
        return n + 1
    elif n == 0:
        return ack(m-1, 1)
    else:
        return ack(m-1, ack(m, n-1))


print(ack(3, 4))  # 125
print(ack(1, 2))  # 4
print(ack(4, 3))  # RecursionError

# For larger values of m and n python can proceed the operation because
# the number of allow recursion call is exceeded
