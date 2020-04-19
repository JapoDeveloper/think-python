"""
Think Python, 2nd Edition
Chapter 10
Exercise 10.5

Description:
 
Write a function called is_sorted that takes a list as a parameter and returns 
True if the list is sorted in ascending order and False otherwise. For example:

    >>> is_sorted([1, 2, 2])
    True
    >>> is_sorted(['b', 'a'])
    False
"""


def is_sorted(t):
    """check if elements in a list are sorted

    Parameters:
        t -> list of elements

    Return -> True or False
    """
    return t == sorted(t)


print(is_sorted([1, 2, 2]))
print(is_sorted(['b', 'a']))
