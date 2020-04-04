"""
Think Python, 2nd Edition
Chapter 1
Exercise 1.1 

Description: try python basics an answer the questions.
"""

# 1) In a print statement, 
# what happens if you leave out one of the parentheses, or both?
print('Hello everybody!')
print('Hello everybody!' # The interpreter throws an error because the syntax is invalid
print 'Hello everybody!' # The interpreter throws an error because parentheses are missing


# 2) If you are trying to print a string, 
# what happens if you leave out one of the quotation marks, or both?
print('I am ok) # The interpreter throws an syntax error 
                # because string close literal doesn't appear
print(I am ok) # The interpreter throws an error because the syntax is invalid

# 3) You can use a minus sign to make a negative number like -2. 
# What happens if you put a plus sign before a number? What about 2++2?
print(-2)   # -2 is printed
print(+2)   # 2 is printed
print(2++2) # 4 is printed, the adition operation is performed

# 4) In math notation, leading zeros are okay, as in 02. 
# What happens if you try this in Python?
print(02) # The interpreter throws an syntax error because is not recognized as a number

# 5) What happens if you have two values with no operator between them?
print(5 4) # The interpreter throws an error because the syntax is invalid