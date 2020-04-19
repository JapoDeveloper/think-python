"""
Think Python, 2nd Edition
Chapter 10
Exercise 10.4

Description:

Write a function called chop that takes a list, modifies it by removing the 
first and last elements, and returns None. For example:

    >>> t = [1, 2, 3, 4]
    >>> chop(t)
    >>> t
    [2, 3]
"""


def chop(t):
    """
    Remove the first and last elements of the list

    Parameters:

        t -> lists of elements

    Return -> None
    """
    del t[0]
    del t[-1]


t = [1, 2, 3, 4]
chop(t)
print(t)
