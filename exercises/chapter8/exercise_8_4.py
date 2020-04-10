"""
Think Python, 2nd Edition
Chapter 8
Exercise 8.4

Description:

The following functions are all intended to check whether a string contains any
lowercase letters, but at least some of them are wrong. For each function,
describe what the function actually does
(assuming that the parameter is a string).

    def any_lowercase1(s):
        for c in s:
            if c.islower():
                return True
            else:
                return False

    def any_lowercase2(s):
        for c in s:
            if 'c'.islower():
                return 'True'
            else:
                return 'False'

    def any_lowercase3(s):
        for c in s:
            flag = c.islower()
        return flag

    def any_lowercase4(s):
        flag = False
        for c in s:
            flag = flag or c.islower()
        return flag

    def any_lowercase5(s):
        for c in s:
            if not c.islower():
                return False
        return True
"""


def any_lowercase1(s):
    # The function only check if the first character is lowercasing
    for c in s:
        if c.islower():
            return True
        else:
            return False


def any_lowercase2(s):
    # Always return the string 'True', because instead of checking the variable
    # c the if statement check the string 'c' that is lowercasing
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'


def any_lowercase3(s):
    # The function return True if the last character of the string is
    # lowercasing otherwise False
    for c in s:
        flag = c.islower()
    return flag


def any_lowercase4(s):
    # The function lookup all characters in the string to find a lowercasing
    # character, if is found the function return True, otherwise return False
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag


def any_lowercase5(s):
    # While the characters in the string are all lowercases the function
    # return True, but if any uppercase character is found the return is False
    for c in s:
        if not c.islower():
            return False
    return True


# The function with the correct definition is any_lowercase4
