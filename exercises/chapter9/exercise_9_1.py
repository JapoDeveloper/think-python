"""
Think Python, 2nd Edition
Chapter 9
Exercise 9.1

Description:
Write a program that reads words.txt and prints only the words with more than 
20 characters (not counting whitespace).
"""

fin = open('words.txt')
for line in fin:
    word = line.strip()
    if len(word) > 20:
        print(word)
fin.close()
