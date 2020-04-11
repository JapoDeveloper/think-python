"""
Think Python, 2nd Edition
Chapter 9
Exercise 9.3

Description:
Write a function named avoids that takes a word and a string of forbidden 
letters, and that returns True if the word doesn’t use any of the forbidden 
letters.

Modify your program to prompt the user to enter a string of forbidden letters 
and then print the number of words that don’t contain any of them. Can you find 
a combination of five forbidden letters that excludes the smallest number of 
words?
"""


def avoids(word, excludes):
    """return True if the word doesn't include any of the excludes letters"""
    for letter in excludes:
        if letter in word:
            return False
    return True


fin = open('words.txt')

forbidden_letters = input('Which letters do you want avoid: ')

count = 0  # number of words doesn't use the forbidden letters
for line in fin:
    word = line.strip()
    if avoids(word, forbidden_letters):
        count += 1
        print(word)

print('{} words doesn\'t use the forbidden letters.'.format(count))

fin.close()
