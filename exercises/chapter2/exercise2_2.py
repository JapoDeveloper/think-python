"""
Think Python, 2nd Edition
Chapter 2
Exercise 2.2 

Description: try some math operations
"""

# The volume of a sphere with radius r is (4/3) * pi * r exp 3.
# What is the volume of a sphere with radius 5?
import math
radius = 5
sphere_volumen = (4/3) * math.pi * (radius**3)
print('Volumen of a sphere with radius {} = {:.2f}'
      .format(radius, sphere_volumen))

# Suppose the cover price of a book is $24.95, but bookstores get a 40% discount.
# Shipping costs $3 for the first copy and 75 cents for each additional copy.
# What is the total wholesale cost for 60 copies?
book_price = 24.95
discount = 24.95 * 0.4
book_final_price = book_price - discount
book_copies = 60
shipping_cost = 3 + (book_copies - 1) * 0.75
total_cost = book_copies * book_final_price + shipping_cost
print('Total cost for {} book copies is {:.2f}'
      .format(book_copies, total_cost))

# If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile),
# then 3 miles at tempo (7:12 per mile) and 1 mile at an easy pace again,
# what time do I get home for breakfast?
leave_home_at = 6 * 60 + 52  # time in minutes
slow_run = (8 + 15 / 60)
fast_run = (7 + 12 / 60)
elapsed_time = 2 * slow_run + 3 * fast_run
back_to_home = leave_home_at + elapsed_time
print('Back to home at {:.0f}:{:.0f}'
      .format(back_to_home // 60, back_to_home % 60))
