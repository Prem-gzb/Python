# Identity Operators : 1.) is 2.) is not
# YouTube Video Link: https://youtu.be/V_r25HbBHA8

"""is and is not are two identity operators and they check if the two objects refer to the same memory location or not and outputs
True or False accordingly.
is operator is different from == or equality operator.
== checks and outputs if the elements of two objects are same. If same, then outputs True otherwise False.
whereas is operator checks if the two objects refer to the same memory location. If yes, then outputs True otherwise False.
"""


a = 10
b = 10
print(id(a)) #outputs the memory location of a
print(id(b)) #outputs the memory location of b
print(a == b) #outputs True
print(a is b) #outputs True

a = "hello"
b = "hello"
print(a == b) #outputs True
print(a is b) #outputs True

a = "hello world"
b = "hello world"
print(id(a))
print(id(b))
print(a == b) #outputs True
print(a is b) #outputs False

lst1 = [1,2,3]
lst2 = [1,2,3]
print(id(lst1)) #outputs memory location of lst1
print(id(lst2)) #outputs memory location of lst2
print(lst1 == lst2) #outputs True
print(lst1 is lst2) #outputs False
print(lst1 is not lst2) #outputs True

lst1 = [1,2,3]
lst2 = lst1
print(lst1)
print(lst2)
print(lst1 is lst2) #outputs True
lst2.append(4)

print(lst1) #outputs [1, 2, 3, 4]
print(lst2) #outputs [1, 2, 3, 4]

lst1 = [1,2,3]
lst2 = lst1.copy()
print(lst1) #outputs [1, 2, 3]
print(lst2) #outputs [1, 2, 3]
print(id(lst1)) #outputs memory location of lst1
print(id(lst2)) #outputs memory location of lst2
lst2.append(4)
print(lst1) #outputs [1, 2, 3]
print(lst2) #outputs [1, 2, 3, 4]

lst1 = [1,2,3]
lst2 = lst1.copy()
print(id(lst1))
print(id(lst2))
lst1.append(4)
print(lst1) #outputs [1, 2, 3, 4]
print(lst2) #outputs [1, 2, 3]

lst1 = [1,2,3]
lst2 = lst1[:]
lst2.append(4)
print(lst1) #outputs [1, 2, 3]
print(lst2) #outputs [1, 2, 3, 4]

lst1 = [1,2,3]
lst2 = lst1[:]
lst1.append(4)
print(lst1) #outputs [1, 2, 3, 4]
print(lst2) #outputs [1, 2, 3]

"""Python for better memory optimization allocates the same memory locations to small integer objects if their values are same.
For this reason, integer objects having similar values in the range of -5 to 256 are allocated same memory block.

Python doc link: https://docs.python.org/3/c-api/long.html#c.PyLong_FromLong
"""

a = 10
b = 10
print(a is b) #outputs True

a = -5
b = -5
print(a is b) #outputs True

a = 257
b = 257
print(a is b) # outputs False
