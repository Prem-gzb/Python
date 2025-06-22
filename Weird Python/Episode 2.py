# YouTube Link: https://youtu.be/wxpiLcbusrQ

"""
Banker's rounding method: If a number is having .5, then it is rounded off to the nearest
EVEN number. For example, round(2.5) will be 3, round(3.5) will be 4 but round(2.6) will be
rounded off to 3 in usual manner because 3 is nearer to 2.6 than 2.
"""

print(round(2.5) == round(3.5)) # Outputs False
print(round(1.5) == round(2.5)) # Outputs True
print(round(1.5)) # Outputs 2
print(round(2.5)) # Outputs 2
print(round(3.5)) # Outputs 4
print(round(2.6)) # Outputs 3