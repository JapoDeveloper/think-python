# Write a function that takes a string as an argument and displays the letters
# backward, one per line


def print_reverse_str(s):
    """print the letters in a string in reverse order"""
    index = len(s) - 1
    while index >= 0:
        print(s[index])
        index -= 1


print_reverse_str('function')


# Fix the error in the following program to print the names
# Jack, Kack, Lack, Mack, Nack, Ouack, Pack, and Quack right

prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
    if letter in ('O', 'Q'):
        print(letter + 'u' + suffix)
    else:
        print(letter + suffix)


# What do you think fruit[:] means?
#   This means that all the characters of the string will be return it
fruit = 'banana'
print(fruit[:])


# Modify 'find' so that it has a third parameter: the index in word where
# it should start looking.

def find(word, letter, start_index):
    """
    Find the index of a letter in a word starting the search at specific index
    """
    index = start_index
    while index < len(word):
        if word[index] == letter:
            return index
        index += 1
    return -1


print(find('Monty python', 'y', 5))


# Encapsulate the looping and counting code in a function named count,
# and generalize it so that it accepts the string and the letter as arguments.

def count(s, letter):
    """return the number of occurrences of a letter in a string"""
    count = 0
    for c in s:
        if c == letter:
            count += 1
    return count


print(count('When i code in python in feel so good', 'i'))


# Fix de bugs in is_reverse function
def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False

    i = 0
    j = len(word2) - 1  # substract 1 to the length of second word

    while j >= 0:  # j would be equal to zero too
        print(i, j)
        if word1[i] != word2[j]:
            return False
        i += 1
        j -= 1

    return True


print(is_reverse('pots', 'stop'))
