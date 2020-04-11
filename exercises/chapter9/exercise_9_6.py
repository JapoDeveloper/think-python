"""
Think Python, 2nd Edition
Chapter 9
Exercise 9.6

Description:
Write a function called is_abecedarian that returns True if the letters in a 
word appear in alphabetical order (double letters are okay). How many 
abecedarian words are there?
"""

from words import list_words


def is_abecedarian(word):
    """check if letters in a word are in alphabetical order"""
    if word is None or len(word) == 0:
        print('Invalid word input')
        return
    previous = word[0]
    for letter in word:
        if previous > letter:
            return False
        previous = letter
    return True


print(is_abecedarian('is'))  # True
print(is_abecedarian('passion'))  # False
print(is_abecedarian('low'))  # True

words = list_words()
abecedarian_count = 0
for word in words:
    if is_abecedarian(word):
        abecedarian_count += 1

print('{} words are abecedarian'.format(abecedarian_count))
