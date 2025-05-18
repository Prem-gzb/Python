# YouTube Video Link: https://youtu.be/UXdl_80aWw8

"""
range function takes three parameters, start value, stop value and step value.
step value is a mandatory parameter while other two are optional.
If only one parameter is given, then it is stop value.
If two parameters are given, then first one is start and second one is stop value.
range starts from start value and ends at stop value excluding the stop value.
The start value by default is 0 and step value by default is 1.
"""

# Define a range
r = range(5)
print(r) # this code will output range object range(0, 5)
print(type(r))
print(list(r)) # this code will convert the range object in list to enable to see individual elements.

# creating a range from custom start value
r = range(5,10)
print(list(r))

# Below code has start value 5, stop value 15 and step value 2
r = range(5,15,2)
print(list(r))

# Negative step value
r1 = range(10,5,-2)
print(list(r1))

# Slicing a range
r = range(5,10)
print(list(r)[0]) # it will output [5]
print(list(r)[10]) # it will product IndexError because range has only 5 elements and we are trying access element at index 10.
r[0] = 50 # this line will produce an TypeError because you can change or mutate a range once created