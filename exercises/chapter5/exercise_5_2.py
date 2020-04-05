"""
Think Python, 2nd Edition
Chapter 5
Exercise 5.2

Description: 

Fermat’s Last Theorem says that there are no positive integers a, b, and c 
such that aˆn + bˆn = cˆn for any values of n greater than 2.

1) Write a function named check_fermat that takes four parameters a, b, c and n
and checks to see if Fermat’s theorem holds. If n is greater than 2 and
aˆn + bˆn = cˆn the program should print, “Holy smokes, Fermat was wrong!” 
Otherwise the program should print, “No, that doesn’t work.”

2) Write a function that prompts the user to input values for a, b, c and n, 
converts them to integers, and uses check_fermat to check whether they violate 
Fermat’s theorem.
"""


def check_fermat(a, b, c, n):
    """
    Checker for the Fermat's Last Theorem
    """
    if n > 2 and ((a**n + b**n) == c**n):
        print('Holy smokes, Fermat was wrong!')
    else:
        print('No, that doesn’t work.')


def get_numbers():
    """
    Capture user input for values to check de Fermat's Theorem
    """
    print('Hello, you are in Fermat\'s Last Theorem checker')
    print('Type:')
    a = int(input('a='))
    b = int(input('b='))
    c = int(input('c='))
    n = int(input('n='))
    return (a, b, c, n)


a, b, c, n = get_numbers()
check_fermat(a, b, c, n)
