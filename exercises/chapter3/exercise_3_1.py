"""
Think Python, 2nd Edition
Chapter 3
Exercise 3.1

Description: 

Write a function named right_justify that takes a string named s as a parameter 
and prints the string with enough leading spaces so that the last letter of the 
string is in column 70 of the display:
"""


def right_justify(s):
    spaces = ' ' * (70 - len(s))
    print(f'{spaces}{s}')


right_justify('monty')
