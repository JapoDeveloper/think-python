"""
Think Python, 2nd Edition
Chapter 6
Exercise 6.3

Description: 
A palindrome is a word that is spelled the same backward and forward, 
like “noon” and “redivider”. Recursively, a word is a palindrome if the first 
and last letters are the same and the middle is a palindrome.

The following are functions that take a string argument and return the first, 
last, and middle letters:

def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]
We’ll see how they work in Chapter 8.

1) Type these functions into a file named palindrome.py and test them out. 
What happens if you call middle with a string with two letters? One letter? 
What about the empty string, which is written '' and contains no letters?

2) Write a function called is_palindrome that takes a string argument and returns 
True if it is a palindrome and False otherwise. Remember that you can use the 
built-in function len to check the length of a string.
"""

from palindrome import *


def is_palindrome(word):
    if len(word) <= 1:
        return True
    elif first(word) == last(word):
        return is_palindrome(middle(word))
    else:
        return False


print(first('Hello'))  # H
print(middle('Hello'))  # ell
print(last('Hello'))   # o

# What happens if you call middle with a string with two letters?
print(middle('ab'))  # empty string is returned

# One letter?
print(middle('a'))  # empty string is returned

# What about the empty string, which is written '' and contains no letters?
print(middle(''))  # empty string is returned

print('Are palindromes?:')
print('noon', is_palindrome('noon'))  # Yes
print('redivider', is_palindrome('redivider'))  # Yes
print('a', is_palindrome('a'))  # Yes
print('empty string', is_palindrome(''))  # Yes
print('night', is_palindrome('night'))  # No
print('word', is_palindrome('word'))  # No
