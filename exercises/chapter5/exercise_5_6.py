"""
Think Python, 2nd Edition
Chapter 5
Exercise 5.6

Description: 

The Koch curve is a fractal that looks something like Figure 5-2. To draw a 
Koch curve with length x, all you have to do is:

1) Draw a Koch curve with length x/3.

2) Turn left 60 degrees.

3) Draw a Koch curve with length x/3.

4) Turn right 120 degrees.

5) Draw a Koch curve with length x/3.

6) Turn left 60 degrees.

7) Draw a Koch curve with length x/3.

The exception is if x is less than 3: in that case, you can just draw a straight 
line with length x.

1) Write a function called koch that takes a turtle and a length as parameters, 
and that uses the turtle to draw a Koch curve with the given length.

2) Write a function called snowflake that draws three Koch curves to make the 
outline of a snowflake.

3) The Koch curve can be generalized in several ways. 
See http://en.wikipedia.org/wiki/Koch_snowflake for examples and implement 
your favorite.
"""

import turtle


def koch(t, length):
    """
    Draw a Koch curve with the given length
    t     : Turtle -> object use to draw into the window 
    length: int    -> the length should have the curve
    """
    if length < 3:
        t.fd(length)
        return

    length /= 3
    koch(t, length)
    t.lt(60)
    koch(t, length)
    t.rt(120)
    koch(t, length)
    t.lt(60)
    koch(t, length)


def snowflake(t, length):
    """
    Draw a snowflake using Koch curve
    t     : Turtle -> object use to draw into the window 
    length: int    -> the length should have the figure
    """
    koch(t, length)
    t.rt(120)
    koch(t, length)
    t.rt(120)
    koch(t, length)


def draw(f, t, length):
    """
    Wrapper function to prepare the workspace before start drawing
    f     : function -> draw function to be called
    t     : Turtle   -> object use to draw into the window
    length: int      -> the length should have the figure
    """
    # Prepare the workspace
    t.pu()
    t.bk(length/2)
    t.pd()

    # Init to draw
    f(t, length)


t = turtle.Turtle()

# draw(koch, t, 100)
draw(snowflake, t, 100)

turtle.mainloop()
