"""Operators are symbols using which operations like addtion, subtraction,
greater than, less than etc can be done on variable and/or values.
"""
# YouTube Video Link: https://youtu.be/WPwUDMCHiO0

x = 10
y = 5
s = "Python"
l = ["Hello World", 10,3.14]

print("x = ", x)
print("y = ", y)
print("s = ", s)
print("l = ", l)

x = 0
x = x + 1
# Addition Assignment Operator
# += is  same as code in line 17 but it's more Pythonic way.
x += 1
print("x = ", x)

x = 10
y = 5
# Again code in 26 and 29 give same result but line 29 is Pythonic way
x = x + y
# += adds the value on right side of operator to left side and saves the
# result in variable on left side.
x += y
print("x = ", x)

x = x- y
# Subtraction Assignment Operator
x -= y
# -= subtracts the value on right side of operator to left side and saves the
# result in variable on left side.
print("x = ", x)

x = x * y
# Multiplication Assignment Operator
# *= multiplies the value on right side of operator to left side and saves the
# result in variable on left side.
x *= y
print("x = ", x)

x = x / y
# Division Assignment Operator
# /= divdes the value on left side of operator with right side and saves the
# result in variable on left side.
x /= y
print("x = ", x)

# Python allows to assign values to more than one varibale in a single line
# Code in line 55 assigns value 6 to both variables a and b.
a = b = 6
print("a =", a)
print("b =", b)

# We can assign different values to different variable also in one
# single line like below.
a, b, c = 6, 8, 18

print("a =", a)
print("b =", b)
print("c =", c)