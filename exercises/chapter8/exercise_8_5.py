"""
Think Python, 2nd Edition
Chapter 8
Exercise 8.5

Description:

A Caesar cypher is a weak form of encryption that involves “rotating” each
letter by a fixed number of places. To rotate a letter means to shift it through
 the alphabet, wrapping around to the beginning if necessary, so ‘A’ rotated by
 3 is ‘D’ and ‘Z’ rotated by 1 is ‘A’.

To rotate a word, rotate each letter by the same amount. For example, “cheer”
rotated by 7 is “jolly” and “melon” rotated by -10 is “cubed”.
In the movie 2001: A Space Odyssey, the ship computer is called HAL, which is
IBM rotated by -1.

Write a function called rotate_word that takes a string and an integer as
parameters, and returns a new string that contains the letters from the original
string rotated by the given amount.

You might want to use the built-in function ord, which converts a character to a
numeric code, and chr, which converts numeric codes to characters. Letters of
the alphabet are encoded in alphabetical order, so for example:

    >>> ord('c') - ord('a')
    2

Because 'c' is the two-eth letter of the alphabet. But beware: the numeric codes
 for uppercase letters are different.

Potentially offensive jokes on the Internet are sometimes encoded in ROT13,
which is a Caesar cypher with rotation 13. If you are not easily offended,
find and decode some of them.
"""


def new_character(c, n):
    """
    Find the character in 'n' position after/before character 'c'.
    """
    # Range of ordinal values of letters in the alphabet
    ref_min, ref_max = (ord('a'), ord(
        'z')) if c.islower() else (ord('A'), ord('Z'))

    # Number of letters in the range
    num_c = ref_max - ref_min + 1

    # As abs(n) can be greatter than letters in the alphabet,
    # instead of do some cycles over the range of letters
    # get a new 'n' equivalent that will be in the range
    n %= num_c if n >= 0 else -num_c

    nc_ord = ord(c) + n  # Hold the new character ordinal value

    # Compute a new letter until it will be in the range
    n -= ref_max - ord(c) if n > 0 else ref_min - ord(c)
    while nc_ord > ref_max or nc_ord < ref_min:
        if n > 0:
            nc_ord = ref_min + n - 1
            n -= ref_max - nc_ord
        else:
            nc_ord = ref_max + n + 1
            n -= nc_ord - ref_min

    return chr(nc_ord)


def rotate_word(word, n):
    """
    Construct a new word moving every character 'n' position forward
    or backward in the alphabet
    """

    if word.isalpha() == False:
        print('Only accept alphabetic words')
        return

    new_word = []
    for c in word:
        new_word.append(new_character(c, n))

    return ''.join(new_word)


print(rotate_word('char2', 5))  # None
print(rotate_word('same', 0))  # same
print(rotate_word('cheer', 7))  # jolly
print(rotate_word('melon', -10))  # cubed
print(rotate_word('melon', -36))  # cubed
print(rotate_word('IBM', -1))  # HAL
print(rotate_word('house', 13))  # ubhfr
print(rotate_word('HOUSE', 13))  # UBHFR
print(rotate_word('python', 99))  # ktocji
