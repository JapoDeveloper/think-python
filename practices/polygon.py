import turtle
import math


def line(t, length, angle):
    """Draw a line with a fixed angle and length.
    t: Turtle      -> the object use to draw in the window
    length: int    -> length of each line
    angle: float   -> value in degrees
    """
    t.lt(angle)
    t.fd(length)


def polyline(t, n, length, angle):
    """Draw n number of lines with a fixed angle and length.
    t: Turtle      -> the object use to draw in the window
    n: int         -> number of lines
    length: int    -> length of each line
    angle: float   -> value in degrees
    """
    for _ in range(n):
        t.fd(length)
        t.lt(angle)


def polygon(t, n, length):
    """Draw a polygon of 'n' sides with a fixed length.
    t: Turtle   -> the object use to draw in the window
    n: int      -> number of sides of the polygon
    length: int -> the length of every polygon side in pixels
    """
    angle = 360.0 / n  # value of the external angle in degrees of a polygon side
    polyline(t, n, length, angle)


def arc(t, r, angle):
    """Draw an arc with fixed angle and radius.
    t: Turtle     -> the object use to draw in the window
    r: int        -> the radius of the circumference
    angle: float  -> value in degrees
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    l_length = arc_length / n
    l_angle = float(angle) / n

    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    t.lt(l_angle/2)
    polyline(t, n, l_length, l_angle)
    t.rt(l_angle/2)


def circle(t, r):
    """Draw a circle of radius 'r'.
    t: Turtle -> the object use to draw in the window
    r: int    -> the radius of the circle
    """
    arc(t, r, angle=360)


if __name__ == '__main__':
    t = turtle.Turtle()

    # Make a circle with radius = 50
    circle(t, 50)

    # Make a equilateral triangle with lenght = 100
    polygon(t, n=3, length=100)

    # Make a square with lenght = 100
    polygon(t, n=4, length=100)

    turtle.mainloop()
