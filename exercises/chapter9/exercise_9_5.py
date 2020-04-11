"""
Think Python, 2nd Edition
Chapter 9
Exercise 9.5

Description:
Write a function named uses_all that takes a word and a string of required 
letters, and that returns True if the word uses all the required letters at 
least once. How many words are there that use all the vowels aeiou? 
How about aeiouy?
"""

from words import list_words


def uses_all(word, letters):
    """return True if the word use all the letters"""
    for letter in letters:
        if letter not in word:
            return False
    return True


print(uses_all('cancer', 'cae'))  # True
print(uses_all('mountain', 'uony'))  # False

words = list_words()
aeiou_count = 0
aeiouy_count = 0
for word in words:
    if uses_all(word, 'aeiou'):
        aeiou_count += 1
    if uses_all(word, 'aeiouy'):
        aeiouy_count += 1

print('{} words using \'aeiou\''.format(aeiou_count))
print('{} words using \'aeiouy\''.format(aeiouy_count))
