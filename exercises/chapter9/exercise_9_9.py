"""
Think Python, 2nd Edition
Chapter 9
Exercise 9.9

Description:
Here’s another Car Talk Puzzler you can solve with a search 
(http://www.cartalk.com/content/puzzlers):

    “Recently I had a visit with my mom and we realized that the two digits that 
    make up my age when reversed resulted in her age. For example, if she’s 73, 
    I’m 37. We wondered how often this has happened over the years but we got 
    sidetracked with other topics and we never came up with an answer.

    “When I got home I figured out that the digits of our ages have been 
    reversible six times so far. I also figured out that if we’re lucky it would 
    happen again in a few years, and if we’re really lucky it would happen one 
    more time after that. In other words, it would have happened 8 times over 
    all. So the question is, how old am I now?”

Write a Python program that searches for solutions to this Puzzler. 
Hint: you might find the string method zfill useful.
"""


def palindromic_age_check(diff, show=False):
    """
    compute the ages that are palindromic with a difference of fixed years, and 
    return the count of occurrences in a century

    Parameters:
        diff :int  -> number of the years between ages
        show :bool -> indicate if the ages will be printed
    """
    count = 0
    for i in range(1, 100):
        child_age = str(i).zfill(2)
        mon_age = str(i + diff).zfill(2)
        if child_age[::-1] == mon_age:
            if show:
                print('child {}, mother {}'.format(child_age, mon_age))
            count += 1
    return count


def age_diff_occurrences(occurrences):
    """compute the difference between ages that satisfy that 
    ages are palindromic a certain times in a century"""
    diff = 10
    while diff < 70:
        count = palindromic_age_check(diff)
        if count == occurrences:
            return diff
        diff += 1


age_diff = age_diff_occurrences(8)  # find the correct ages difference

print('The ages that statisfy the problem are:')
palindromic_age_check(age_diff, show=True)
