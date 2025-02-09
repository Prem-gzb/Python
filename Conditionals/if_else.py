# YouTube Video Link: https://youtu.be/MDAZSjcz1Xo

# program to check if the num is positive
num = 3
if num > 0:
    print(f"{num} is positive")
print("End of Program")

# program to check if the num is positive or negative
num = 3
if num < 0:
    print(f"{num} is positive")
else:
    print(f"{num} is negative")
print("End of Program")

# program to check multiple condition using elif
num = 0
if num > 0:
    print(f"{num} is positive")
elif num == 0:
    print("It's Zero")
else:
    print(f"{num} is negative")
print("End of Program")


# program to check multiple condition using elif
# The order in which conditions are placed are important
marks = int(input("Enter marks: "))

if marks > 80:
    print("A")
elif marks > 60:
    print("B")
elif marks > 40:
    print("C")
else:
    print("D")

# In the program, the order of condition is reversed, therefore, it first checks
# if the marks is greater than 40. Hence even if the marks is 85, it will print C.

# Moral is once a condition under if or elif is satisfied, program does not check further
# conditions under elif clause.
marks = int(input("Enter marks: "))

if marks > 40:
    print("C")
elif marks > 60:
    print("B")
elif marks > 80:
    print("A")
else:
    print("D")

# The condition and corresponding action need not be on separate lines. These
# can be on the same line.

marks = int(input("Enter marks: "))

if marks > 40:print("C")
elif marks > 60:print("B")
elif marks > 80:print("A")
else:print("D")