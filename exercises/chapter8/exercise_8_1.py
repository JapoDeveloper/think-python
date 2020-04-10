"""
Think Python, 2nd Edition
Chapter 8
Exercise 8.1

Description:

Read the documentation of the string methods at 
http://docs.python.org/3/library/stdtypes.html#string-methods. You might want 
to experiment with some of them to make sure you understand how they work. 
strip and replace are particularly useful.

The documentation uses a syntax that might be confusing. For example, 
in find(sub[, start[, end]]), the brackets indicate optional arguments. So sub 
is required, but start is optional, and if you include start, 
then end is optional.
"""

# str.capitalize()
print('test'.capitalize())  # Test

# str.casefold()
print('ß'.casefold())  # ss

# str.center(width[, fillchar])
print('Hello'.center(10))
print('World'.center(10, '*'))

# str.count(sub[, start[, end]])
print('chocolate'.count('o'))       # 2
print('chocolate'.count('o', 3))    # 1
print('chocolate'.count('o', 1, 5))  # 2

# str.encode(encoding="utf-8", errors="strict")
print('secret'.encode())  # b'secret'

# str.endswith(suffix[, start[, end]])
print('record'.endswith('rd'))             # True
print('record'.endswith('o', 0, 4))        # True
print('record'.endswith(('r', 'd'), 0, 2))  # False

# str.expandtabs(tabsize=8)
print('01\t2345\t6789'.expandtabs(tabsize=3))  # 01 2345  6789

# str.find(sub[, start[, end]])
print('ark'.find('c'))              # -1
print('overnight'.find('night', 2))  # 4

# str.format(*args, **kwargs)
print('{} four people are in {site} when {someone} enter'.format(
    4, site='the house', someone='Kite'))

# str.format_map(mapping)
print('The {animal} bit me, and on the {day} day it die'.format_map({
    'animal': 'Cobra', 'day': 'second'
}))

# str.index(sub[, start[, end]])
try:
    print('ark'.index('c'))
except ValueError as e:
    print(e)
print('overnight'.index('night', 2))  # 4

# str.isalnum()
print('2tapk'.isalnum())  # True
print('**&'.isalnum())  # False

# str.isalpha()
print('Cat'.isalpha())  # True

# str.isascii()
print('\n'.isascii())  # True

# str.isdecimal()
print('1024'.isdecimal())  # True

# str.isdigit()
print('1024'.isdigit())  # True

# str.isidentifier()
print('length'.isidentifier())  # True
print('4length'.isidentifier())  # False

# str.islower()
print('Current'.islower())  # False

# str.isnumeric()
print('1234'.isnumeric())  # True

# str.isprintable()
print('abc'.isprintable())  # True
print('\n'.isprintable())  # False

# str.isspace()
print('  \t  \n'.isspace())  # True

# str.istitle()
print('Titulo 1'.istitle())  # True

# str.isupper()
print('ABC'.isupper())  # True

# str.join(iterable)
print(','.join(['1', '2', '3', '4', '5']))  # 1,2,3,4,5

# str.ljust(width[, fillchar])
print('Ana'.ljust(4, '_'))  # Ana_

# str.lower()
print('LOWER'.lower())  # lower

# str.lstrip([chars])
print('http:\\google.com'.lstrip('htp:\\'))  # google.com

# static str.maketrans(x[, y[, z]])
print('abc'.maketrans({'a': 1, 'b': 2, 'c': 3}))

# str.partition(sep)
print('x = 2+2'.partition('='))  # ('x', '=', '2+2')

# str.replace(old, new[, count])
print('Alex open the door, look a chair. Alex sit down, and Alex drink a cup of water.'.replace(
    'Alex', 'John', 2))

# str.rfind(sub[, start[, end]])
print('overnight'.rfind('er'))  # 2

# str.rindex(sub[, start[, end]])
try:
    print('ark'.rindex('c'))
except ValueError as e:
    print(e)
print('overnight'.rindex('night', 2))  # 4

# str.rjust(width[, fillchar])
print('Ana'.rjust(4, '_'))  # _Ana

# str.rpartition(sep)
print('x = y = 2+2'.rpartition('='))  # ('x = y', '=', '2+2')

# str.rsplit(sep=None, maxsplit=-1)
print('apple\tbanana\tcereal'.rsplit(
    sep='\t', maxsplit=1))  # ['apple\tbanana', 'cereal']

# str.rstrip([chars])
print('exponentiation'.rstrip('otina'))  # expone

# str.split(sep=None, maxsplit=-1)
print('apple\tbanana\tcereal'.split(
    sep='\t'))  # ['apple', 'banana', 'cereal']

# str.splitlines([keepends])
print('one\ntwo\rthree\r\n'.splitlines())  # ['one', 'two', 'three']

# str.startswith(prefix[, start[, end]])
print('record'.startswith('e', 1))  # True

# str.strip([chars])
print('http:\\google.com'.strip('hctop:.\\m'))  # google

# str.swapcase()
print('LOWER upper'.swapcase())  # lowe UPPER

# str.title()
print('python exercises'.title())  # Python Exercises

# str.translate(table)
print('abc'.translate(''.maketrans({'a': 'b', 'b': 'c'})))  # bcc

# str.upper()
print('all the letter must be upper'.upper())

# str.zfill(width)
print('5'.zfill(3))  # 005
print('+5'.zfill(3))  # +05
print('-5'.zfill(3))  # -05
