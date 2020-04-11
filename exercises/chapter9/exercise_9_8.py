"""
Think Python, 2nd Edition
Chapter 9
Exercise 9.8

Description:
Here’s another Car Talk Puzzler (http://www.cartalk.com/content/puzzlers):

    “I was driving on the highway the other day and I happened to notice my 
    odometer. Like most odometers, it shows six digits, in whole miles only. So, 
    if my car had 300,000 miles, for example, I’d see 3-0-0-0-0-0.

    “Now, what I saw that day was very interesting. I noticed that the last 4 
    digits were palindromic; that is, they read the same forward as backward. 
    For example, 5-4-4-5 is a palindrome, so my odometer could have 
    read 3-1-5-4-4-5.

    “One mile later, the last 5 numbers were palindromic. For example, it could 
    have read 3-6-5-4-5-6. One mile after that, the middle 4 out of 6 numbers 
    were palindromic. And you ready for this? One mile later, all 6 were 
    palindromic!
å
    “The question is, what was on the odometer when I first looked?”

Write a Python program that tests all the six-digit numbers and prints any 
numbers that satisfy these requirements.
"""


from words import is_palindrome


def has_palindrome(s, start, length):
    """check if a portion of a string is a polindrome"""
    return is_palindrome(s[start:start+length])


def apply(i):
    """
    check if a integer follows certains rules:
        1) the last 4 digits of the number is a palindrome
        2) the last 5 digits of the number + 1 is a palindrome
        3) the middle 4 digits of the number + 2 is a palindrome
        4) the last 6 digits of the number + 3 is a palindrome
    """
    d1, d2, d3, d4 = str(i), str(i+1), str(i+2), str(i+3)
    return (has_palindrome(d1, 2, 4) and has_palindrome(d2, 1, 5) and
            has_palindrome(d3, 1, 4) and has_palindrome(d4, 0, 6))


print('The first odometer value could be:')
for i in range(100000, 999997):
    if apply(i):
        print(i)
