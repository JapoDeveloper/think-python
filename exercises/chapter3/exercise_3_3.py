"""
Think Python, 2nd Edition
Chapter 3
Exercise 3.3

Description:

Write a function that draws a grid like the following:

+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +

Write a function that draws a similar grid with four rows and four columns.
"""


def do_twice(f, arg):
    f(arg)
    f(arg)


def do_four(f, arg):
    do_twice(f, arg)
    do_twice(f, arg)


def plus_sequence(n):
    """
    Create the pattern for top-bottom side of a grid
    n: int -> the number of times the pattern will be repeated
    """
    pattern = '- ' * int(8//2)
    return ('+ ' + pattern) * n + '+'


def bar_sequence(n):
    """
    Create the pattern for left-right side of a grid
    n: int -> the number of times the pattern will be repeated
    """
    pattern = ' ' * 8
    return ('| ' + pattern) * n + '|'


def print_sequence(s):
    print(s)


def draw_row_grid(n):
    """
    Print a row of the grid with n columns
    n          : int  -> the number columns
    """
    print_sequence(plus_sequence(n))
    do_four(print_sequence, bar_sequence(n))


def draw_grid_1_1():
    n = 1
    draw_row_grid(n)
    print_sequence(plus_sequence(n))


def draw_grid_2_2():
    n = 2
    do_twice(draw_row_grid, n)
    print_sequence(plus_sequence(n))


def draw_grid_4_4():
    n = 4
    do_four(draw_row_grid, n)
    print_sequence(plus_sequence(n))


draw_grid_1_1()
draw_grid_2_2()
draw_grid_4_4()
