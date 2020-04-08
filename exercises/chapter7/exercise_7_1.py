"""
Think Python, 2nd Edition
Chapter 7
Exercise 7.1

Description:

Copy the loop from “Square Roots” and encapsulate it in a function called mysqrt
that takes a as a parameter, chooses a reasonable value of x, and returns an
estimate of the square root of a.

To test it, write a function named test_square_root that prints a table
like this:

    a   mysqrt(a)     math.sqrt(a)  diff
    -   ---------     ------------  ----
    1.0 1.0           1.0           0.0
    2.0 1.41421356237 1.41421356237 2.22044604925e-16
    3.0 1.73205080757 1.73205080757 0.0
    4.0 2.0           2.0           0.0
    5.0 2.2360679775  2.2360679775  0.0
    6.0 2.44948974278 2.44948974278 0.0
    7.0 2.64575131106 2.64575131106 0.0
    8.0 2.82842712475 2.82842712475 4.4408920985e-16
    9.0 3.0           3.0           0.0

The first column is a number, a; the second column is the square root of a
computed with mysqrt; the third column is the square root computed by math.sqrt;
the fourth column is the absolute value of the difference between
the two estimates.
"""

import math


def mysqrt(a):
    """Calculate the square root of a number 'a'"""
    x = a / 5  # initial aproximation of the result
    epsilon = 0.0000001  # indicates the result closest aproximation accepted
    while True:
        y = (x + a / x) / 2
        if abs(y - x) < epsilon:
            return y
        x = y


def test_square_root():
    """Execute a test over mysqrt and math.sqrt functions"""
    print('{:<3}'.format('a'),
          '{:<13}'.format('mysqrt(a)'),
          '{:<13}'.format('math.sqrt(a)'),
          '{:<13}'.format('diff'))
    print('{:<3}'.format('-'),
          '{:<13}'.format('---------'),
          '{:<13}'.format('------------'),
          '{:<13}'.format('----'))
    for a in range(1, 10):
        my_r = mysqrt(a)
        math_r = math.sqrt(a)
        print(
            '{:<3.1f}'.format(a),
            '{:<13}'.format(round(my_r, 11)),
            '{:<13}'.format(round(math_r, 11)),
            '{:<13}'.format(round(abs(my_r - math_r), 27))
        )


test_square_root()
