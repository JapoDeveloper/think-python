"""
Think Python, 2nd Edition
Chapter 9
Exercise 9.4

Description:
Write a function named uses_only that takes a word and a string of letters, 
and that returns True if the word contains only letters in the list. 
Can you make a sentence using only the letters acefhlo? Other than 
“Hoe alfalfa?”
"""

from words import list_words
import random


def make_sentence(letters, words_count):
    """construct a sentence with words that only use the given letters and with 
    a specific count of words"""
    words = []  # hold all the words that follows the rule
    for word in list_words():
        if uses_only(word, letters):
            words.append(word)

    selected_words = []
    for _ in range(words_count):
        index = random.randint(0, len(words))
        selected_words.append(words[index])
    return ' '.join(selected_words)


def uses_only(word, letters):
    """return true if word only use a set letters"""
    letters = letters.lower()
    for letter in word:
        if letter.lower() not in letters:
            return False
    return True


print(uses_only('Hoe', 'acefhlo'))
print(uses_only('alfalfa', 'acefhlo'))
print(make_sentence('acefhlo', 6))
