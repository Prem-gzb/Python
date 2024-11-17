# YouTube Video Link
# Bitwise Operator Part 1: https://youtu.be/hRzqmG8BP-M
# Bitwise Operator Part 2: https://youtu.be/RX06x2phz5c


"""Bitwise Operators
There are six bitwise operators, viz., AND, OR, XOR, NOT, Bitwise Left Shift and Bitwise Right Shift.
Any number passed on as argument is first converted into Binary Number system before these operators work upon them.
"""


"""Conversion from Decimal to Binary Number System"""

a = 10
b = 1
print(bin(a))
print(bin(b))
print(bin(2))

# 0b in the beginning represents binary number base. If you want only the number, then use
# print(bin(a)[2:])

"""Conversion from Binary to Decimal Number System"""
# print(int("1010",2)) #outputs 10 in decimal
# print(int("0b1010", 2)) #outputs 10 in decimal

"""AND Operator
It takes two operands and returns 1 if both bits are 1 otherwise returns 0.
It is denoted using ampersand (&) sign
"""
print(10 & 1) #outputs 0
print(10 & 2) #outputs 2

# Explanation
# print(10 & 1)
# 10 in binary = 1010
# 1 in binary = 1
# 1010
# 0001
# ====
# 0000

# print(10 & 2)
# 10 in binary = 1010
# 2 in binary = 10
# 1010
# 0010
# ====
# 0010

"""OR Operator
# It takes two operands and returns 1 if any of the bits are 1 else returns 0.
It is denoted using pipe (|) symbol.
"""

print(10 | 1) # outputs 11

# Explanation
# 10 in binary = 1010
# 1 in binary = 1
# 1010
# 0001
# ====
# 1011
# 1011 in decimal = 11

"""XOR or Exclusive OR Operator
It returns True (or 1) if both bits are different else returns False (or 0).
It is denoted using caret(^) symbol.
"""

print(10 ^ 1) # outputs 11

# Explanation
# 1010
# 0001
# ====
# 1011

# 1011 in decimal = 11

"""NOT Operator
It takes only one operand or Unary Operator and inverts or reverses the values of bits.
It is denoted using tilde (~) symbol.
"""
a = 10
print(~a) # outputs -11

"""Bitwise Left Shift Operator
The left operand's value is moved left by specified number of bits or gain the bits
The final output is X * 2 ** n
It is denoted by two greater than (>>) symbol.
"""

a = 10
print(a << 1) #outputs 20
print( a << 2) #outputs 40

"""Bitwise Right Shift Operator
The left operand's value is moved right by specified number of bits or loose the bits.
The final output is X / 2 ** n
It is denoted using two less than (<<) symbol.
"""

a = 10
print(a >> 1) #outputs 5
print(a >> 2) #outptus 2