"""Simple Easy Python
YouTube Video Link: https://youtu.be/o8XX5FUhNfI
"""

"""Comparison or relational operators compare the value or variable on the left-hand side of the operator sign 
with the value or variable on the right-hand side and return the result as the case may be.
"""

"""Double equal to sign is for checking the equality on the two sides of the operator.
It should not be confused with single equal to sign which is used for assigning the value on
the right side of the equal to operator to the variable on the left-hand side.
"""

""" Equality Operator or == """
print(10 == 11)
a = 2
b = 3
print(a == b)
print(10 == 10)
print("cat" == "dog")

"""!= This is for checking inequality on the two sides of the operator. If the value/variable
are not equal, then it returns True otherwise False."""

print(10 != 10)
print("cat" != "dog")
print(a != b)

"""> It checks if the value/variable on the left side of the operator is greater than the 
value/variable on the right side. If yes, then it returns True, otherwise False"""

print(a > b)
print(10 > 5)

"""< It checks if the value/variable on the left side of the operator is less than the 
value/variable on the right side. If yes, then it returns True, otherwise False"""

print(a < b)
print(10 > 11)

""">= It checks if the value/variable on the left side of the operator is greater than or equal to the 
value/variable on the right side. If yes, then it returns True, otherwise False"""
print(10 >= 5)
print(b >= a )

"""<= It checks if the value/variable on the left side of the operator is less than or equal to the 
value/variable on the right side. If yes, then it returns True, otherwise False"""
print(a <= b)
print(10 <= 11)
print(10 <= 5)

"""Bonus tip 1: Python is case sensitive.Cat,cAt, caT. All these are different for Python.
"""
print("cat" == "Cat")

""" Bonus tip 2: Be careful while comparing a string type with integer or float type. It will return False
"""
print("10" == 10)
print(type(10))
print(type("10"))
print(10 == 10.0)