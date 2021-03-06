"""
Think Python, 2nd Edition
Chapter 5
Exercise 5.3

Description: 

If you are given three sticks, you may or may not be able to arrange them 
in a triangle. For example, if one of the sticks is 12 inches long and the 
other two are one inch long, you will not be able to get the short sticks to 
meet in the middle. For any three lengths, there is a simple test to see if it 
is possible to form a triangle:

    If any of the three lengths is greater than the sum of the other two, then 
    you cannot form a triangle. Otherwise, you can. (If the sum of two lengths 
    equals the third, they form what is called a “degenerate” triangle.)

1) Write a function named is_triangle that takes three integers as arguments, 
and that prints either “Yes” or “No”, depending on whether you can or cannot 
form a triangle from sticks with the given lengths.

2) Write a function that prompts the user to input three stick lengths, 
converts them to integers, and uses is_triangle to check whether sticks with 
the given lengths can form a triangle.
"""


def is_triangle(a, b, c):
    """
    Check if the given length for three sticks can  form a triangle
    a,b,c : int -> the length of every side
    """
    if a < (b + c) and b < (a + c) and c < (a + b):
        print('Si')
        return True
    else:
        print('No')
        return False


def get_lengths():
    """
    Prompt user to type the value of three side of a triangle 
    """
    print('Hello, you are in Triangle Checker')
    print('Type:')
    a = int(input('Side 1 length = '))
    b = int(input('Side 2 length = '))
    c = int(input('Side 3 length = '))
    return a, b, c


a, b, c = get_lengths()  # User values
is_triangle(a, b, c)
