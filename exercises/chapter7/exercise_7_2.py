"""
Think Python, 2nd Edition
Chapter 7
Exercise 7.2

Description: 

The built-in function eval takes a string and evaluates it using the Python 
interpreter. For example:

    >>> eval('1 + 2 * 3')
    7
    >>> import math
    >>> eval('math.sqrt(5)')
    2.2360679774997898
    >>> eval('type(math.pi)')
    <class 'float'>

Write a function called eval_loop that iteratively prompts the user, takes the 
resulting input and evaluates it using eval, and prints the result.

It should continue until the user enters 'done', and then return the value of 
the last expression it evaluated.
"""


def eval_loop():
    """Allow user to enter expressions and check its evaluation"""
    result = None
    while True:
        exp = input('>>> ')
        if exp == 'done':
            return result
        try:
            result = eval(exp)
            print(result)
        except Exception as ex:
            print('Invalid expresion!', ex)


print('\nLast result:', eval_loop())
