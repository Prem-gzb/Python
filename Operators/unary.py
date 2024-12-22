"""Unary Operators unlike any other operator take only one operand on their right hand side and produce results.
There are two unary operators in Python. These are logical not and bitwise not operators.
YouTube video link: https://youtu.be/9-ynHVicWoU
"""

print(not True) # outputs False
print(not False) # outputs True

"""Logical Not"""

# Practical example 1
# Below code can be used to ascertain if the list is empty or not using logical not operator

# The below code outputs List is emtpy
lst = []
print(bool(lst))

if not lst:
    print("List is empty")
else:
    print("List is not empty")

# The below code outputs List is not emtpy
lst = [1,2,3]
print(bool(lst))

if not lst:
    print("List is empty")
else:
    print("List is not empty")


# Practical example 2
# Below code again using logical not operator will keep the while loop infinite till the time
# Enter Your Name field is blank.

name = ""

while not name:
    name = input("Enter Your Name: ")
print("Welcome, ", name)

"""Bitwise Not"""

"""Bitwise operators work upon binary numbers
Bitwise not operator inverses the binary number, that is, it will convert 1 into 0 and
0 into 1. It is denoted using tilde (~)
Simply put, bitwise not will increase the positive number by 1 and prefix it with a negative sign
Thus 10 upon using bitwise not will output -11, 5 will output -6 and likewise.
I have explained it in detailed in another video, link of which is given below:
YouTube Video Link: https://youtu.be/RX06x2phz5c
"""

a = 10
print(~a) # outputs -11

b = 5
print(~b) # outputs -6