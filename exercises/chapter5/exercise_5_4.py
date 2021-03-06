"""
Think Python, 2nd Edition
Chapter 5
Exercise 5.4

Description: 

What is the output of the following program? Draw a stack diagram that shows the 
state of the program when it prints the result.

def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)

recurse(3, 0)

1) What would happen if you called this function like this: recurse(-1, 0)?

2) Write a docstring that explains everything someone would need to know in 
order to use this function (and nothing else).
"""

# Stack Diagram
#
#   __main__    |                 |
#   recurse     | n -> 3   s -> 0 |
#   recurse     | n -> 2   s -> 3 |
#   recurse     | n -> 1   s -> 5 |
#   recurse     | n -> 0   s -> 6 |


# Answers

# What is the output of the following program?
#   The programs print 6

# What would happen if you called this function like this: recurse(-1, 0)?
#   The program throws an error because the function will be called infinitly,
#   because n always be lower than 0


def recurse(n, s):
    """
    Perform the sum of numbers from 1 to 'n' and print the result of sum
    it with 's'.

    n: int -> must be greater that zero.
    s: int -> must be greater that equals zero.
    """
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)


recurse(3, 0)
