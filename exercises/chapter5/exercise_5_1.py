"""
Think Python, 2nd Edition
Chapter 5
Exercise 5.1

Description: 

The time module provides a function, also named time, that returns the current 
Greenwich Mean Time in “the epoch”, which is an arbitrary time used as a 
reference point. On UNIX systems, the epoch is 1 January 1970.

>>> import time
>>> time.time()
1437746094.5735958

Write a script that reads the current time and converts it to a time of 
day in hours, minutes, and seconds, plus the number of days since the epoch.
"""

import time

day_secs = 24 * 60 * 60
hour_secs = 60 * 60
min_secs = 60

seconds_since_epoch = time.time()

# Option 1: print the time as a combination of units
days = int(seconds_since_epoch // day_secs)
remaining = seconds_since_epoch - (days * day_secs)

hours = int(remaining // hour_secs)
remaining = remaining - (hours * hour_secs)

minutes = int(remaining // min_secs)
remaining = remaining - (minutes * min_secs)

print(f'Since epoch elapsed {days} days, {hours} hours, {minutes} minutes and {remaining:.2f} seconds')

# Option 2: print the time in every unit independently
days = int(seconds_since_epoch // day_secs)
hours = int((seconds_since_epoch // hour_secs))
minutes = int((seconds_since_epoch // min_secs))
print('Since epoch elapsed:')
print(f'{days} days')
print(f'{hours} hours')
print(f'{minutes} minutes')
print(f'{int(seconds_since_epoch)} seconds')