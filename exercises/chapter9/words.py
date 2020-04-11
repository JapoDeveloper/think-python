"""
Helper functions that will be used in several exercises into the chapter
"""


def list_words():
    """return a list of words"""
    fin = open('words.txt')
    words = []
    for line in fin:
        words.append(line.strip())
    fin.close()
    return words


def is_palindrome(s):
    """check if a string is a palindrome"""
    return s == s[::-1]
