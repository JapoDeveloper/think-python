"""
Think Python, 2nd Edition
Chapter 10
Exercise 10.1

Description:

Write a function called nested_sum that takes a list of lists of integers and 
adds up the elements from all of the nested lists. For example:

    >>> t = [[1, 2], [3], [4, 5, 6]]
    >>> nested_sum(t)
    21

"""


def nested_sum(values):
    """compute the sum of all elements into the given list"""
    acc = 0
    for v in values:
        acc += sum(v)
    return acc


t = [[1, 2], [3], [4, 5, 6]]
print(nested_sum(t))
