# YouTube Video Link: https://youtu.be/1o9oPR1lASk
# f strings were added to Python 3.6 and they allow to embed expression inside string literals.

# Variable Replacement

f_name = "James"
l_name = "boNd"

print(f"Name is {l_name}, {f_name} {l_name}")
print(f"Name is {l_name.title()}, {f_name.upper()} {l_name}")

price = 100
discount = 0.2
print(f"Price = ${price}, discount = {discount:.1%}, final price = ${price * (1 - discount)}")

# format specifiers
# :.(number)f => upto that many decimal digits
# :< => left justify
# :> => right justify
# :^ => centre align
# :, or :_ => uses comma or underscore as thousand separator
# :+ => displays positive (+) sign before positive numbers
# :04 => zero padding on the left side
# :.(number)% => percent

num = 100000
print(f"{num:#<15,}")
print(f"{num:>15}")
print(f"{num:^15}")
print(f"{num:,}")
print(f"{num:_}")

# Time formatting
# :%B => Full Month Name
# :%Y => 4-digit year.
# :%y => 2-digit year.
# :%m => 2-digit month (01-12)
# :%d => 2-digit day of the month (01-31)
# :%H => 2-digit hour (00-23)
# :%M => 2-digit minute (00-59)
# :%S => 2-digit second (00-59)
# :%I => 12 hour clock
# :%p => AM or PM

from datetime import datetime
to_day = datetime.now()
print(to_day)
# print(f"{to_day:%B %d, %Y}")
# print(f"{to_day:%B %d, %y}")
print(f"{to_day:%d-%m-%Y}")
# print(f"{to_day:%m-%d-%Y}")
print(f"{to_day:%d-%m-%Y %H:%M}")
print(f"{to_day:%d-%m-%Y %I:%M:%S %p}")

# Number Conversion from One System to Another

print(f"20 in binary = {20:b}")
print(f"20 in octal = {20:o}")
print(f"20 in hexadecimal = {20:02X}")
print(f"10100 in decimal = {0b10100:d}")

# Printing curly braces
print(f"{{}}")