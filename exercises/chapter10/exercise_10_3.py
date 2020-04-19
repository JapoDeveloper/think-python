"""
Think Python, 2nd Edition
Chapter 10
Exercise 10.3

Description:

Write a function called middle that takes a list and returns a new list that 
contains all but the first and last elements. For example:

    >>> t = [1, 2, 3, 4]
    >>> middle(t)
    [2, 3]
"""


def middle(elements):
    """compute a new list that not include the first and last elements"""
    return elements[1:len(elements)-1]


t = [1, 2, 3, 4]
print(middle(t))

t2 = ['a', 'b', 'c', 'd', 'y', 'z']
print(middle(t2))
