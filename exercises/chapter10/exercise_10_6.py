"""
Think Python, 2nd Edition
Chapter 10
Exercise 10.6

Description:

Two words are anagrams if you can rearrange the letters from one to spell the 
other. Write a function called is_anagram that takes two strings and returns 
True if they are anagrams. 
"""


def is_anagram(word1, word2):
    """check if two words are anagrams"""
    return sorted(word1) == sorted(word2)


print(is_anagram("debit card", "bad credit"))  # True
print(is_anagram("coronavirus", "carnivorous"))  # True
print(is_anagram("pet", "tap"))  # False
