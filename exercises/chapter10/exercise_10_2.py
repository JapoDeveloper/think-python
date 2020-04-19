"""
Think Python, 2nd Edition
Chapter 10
Exercise 10.2

Description:

Write a function called cumsum that takes a list of numbers and returns the 
cumulative sum; that is, a new list where the ith element is the sum of the 
first i+1 elements from the original list. For example:

    >>> t = [1, 2, 3]
    >>> cumsum(t)
    [1, 3, 6]
"""


def cumsum(elements):
    """return a list with the cumulative sum of element"""
    acc = elements[:1]
    for i in range(1, len(elements)):
        acc.append(acc[i-1] + elements[i])
    return acc


t = [1, 2, 3]
t2 = [2, 4, 16]
print(cumsum(t))
print(cumsum(t2))
