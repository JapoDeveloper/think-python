"""
Think Python, 2nd Edition
Chapter 1
Exercise 1.2 

Description: try math operations and answer the questions
"""

# 1) How many seconds are there in 42 minutes 42 seconds?
print(42 * 60 + 42)  # 2,562 seconds

# 2) How many miles are there in 10 kilometers?
# Hint: there are 1.61 kilometers in a mile.
print(10 / 1.61)  # 6.21 miles

# 3) If you run a 10 kilometer race in 42 minutes 42 seconds,
# what is your average pace (time per mile in minutes and seconds)?
# What is your average speed in miles per hour?

race_in_miles = 10 / 1.61
race_time_in_sec = (42 * 60 + 42)
total_mile_time_in_sec = race_time_in_sec / race_in_miles
time_per_mile_in_min = int(total_mile_time_in_sec // 60)
time_per_mile_in_sec = total_mile_time_in_sec % 60

print('Average pace: {} minutes {:.2f} seconds'
      .format(time_per_mile_in_min, time_per_mile_in_sec))

race_time_in_hr = race_time_in_sec / 3600
speed = race_in_miles / race_time_in_hr

print('Average speed: {:.2f} mi/h'.format(speed))
