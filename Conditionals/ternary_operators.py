# YouTube Video Link: https://youtu.be/mxlRu6IY0wo

"""
Shorter way of writing conditional expressions.
if elif else are written in one single line instead of multiple lines.
Ternary Operators are conditional expressions.
Something like question mark operator in Java.
Return True or False (Boolean) basis the evaulation of conditon

value_1 if condition is True else value_2 (when condition is False)
value_1 if condition 1 is True else value_2 if condition 2 is True else value_3
"""

# Convention way of checking if a number is positive or negative using if else construct
num = int(input("Enter number: "))
if num > 0:
    print("Positive")
else:
    print("Negative")

# Ternary Operator to check whether a number is positive or negative
num = int(input("Enter number: "))
print("Positive" if num > 0 else "Negative")

# Nested Ternary Operator equivalent to if elif else construct
num = int(input("Enter number: "))
print("Positive" if num > 0 else "Zero" if num == 0 else "Negative")





