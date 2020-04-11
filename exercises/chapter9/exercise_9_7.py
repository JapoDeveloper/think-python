"""
Think Python, 2nd Edition
Chapter 9
Exercise 9.7

Description:
This question is based on a Puzzler that was broadcast on the radio program
Car Talk (http://www.cartalk.com/content/puzzlers):

    Give me a word with three consecutive double letters. I’ll give you a couple
    of words that almost qualify, but don’t. For example, the word committee,
    c-o-m-m-i-t-t-e-e. It would be great except for the ‘i’ that sneaks in
    there. Or Mississippi: M-i-s-s-i-s-s-i-p-p-i. If you could take out those
    i’s it would work. But there is a word that has three consecutive pairs of
    letters and to the best of my knowledge this may be the only word. Of course
    there are probably 500 more but I can only think of one. What is the word?

Write a program to find it.
"""

from words import list_words


def is_three_doubles(word):
    """check if a word have three consecutive double letters."""
    if word is None or len(word) < 6:
        return False
    consecutives = 0
    index = 0
    while index < len(word) - 1:
        if word[index+1] == word[index]:
            consecutives += 1
            if consecutives == 3:
                return True
            index += 2
        else:
            consecutives = 0
            index += 1
    return False


print(is_three_doubles('Mississippi'))  # False
print(is_three_doubles('Missssppi'))  # True

words = list_words()
for word in words:
    if is_three_doubles(word):
        print(word)

# The word is bookkeeper
