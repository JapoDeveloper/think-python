"""
Think Python, 2nd Edition
Chapter 10
Exercise 10.7

Description:

Write a function called has_duplicates that takes a list and returns True
if there is any element that appears more than once. It should not modify
the original list.
"""


def has_duplicates(t):
    """check if any element of a list appears more than once

    Parameters:
        t -> list of values

    Return -> True or False
    """
    for i, e in enumerate(t):
        if t.index(e) != i:
            return True
    return False


print(has_duplicates([1, 2, 3, 4, 1, 5, ]))  # True
print(has_duplicates([True, False, False]))  # True
print(has_duplicates(['a', 'b', 'c']))  # False
