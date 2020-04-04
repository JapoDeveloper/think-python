"""
Think Python, 2nd Edition
Chapter 2
Exercise 2.1 

Description: try with statements
"""

# We’ve seen that n = 42 is legal. What about 42 = n?
42 = n  # this statement is ilegal, is a syntax error because a varibale
# values will be placed at the right side of the statement

# How about x = y = 1?
x = y = 1  # it is a legal assignment, in this case the value 1 will be
# assign to x and y simultaneosly

# In some languages every statement ends with a semicolon, ;.
# What happens if you put a semicolon at the end of a Python statement?
z = 5  # syntactically is rigth, but not necessary

# What if you put a period at the end of a statement?
a = 1.  # syntactically is rigth for number values
b = ''.  # for string isn't legal

# In math notation you can multiply x and y like this: xy.
# What happens if you try that in Python?
c = 2
d = 3
e = cd  # in python isn't valid, because the interpreter
# try to localize the variable with the compound name cd
# but is not define, causing an NameError
