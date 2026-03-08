# YouTube Video Link:https://youtu.be/5qmK55RUZPw

# Function using print
def add(a,b):
    print(a + b)
add(1,2)
# Below line prints 3, 3 and The sum of two numbers is: None
print("The sum of two numbers is: ", add(1,2))

# Using return statement
def add(a,b):
    c = a + b # assigning sum of a and b to third varaible c
    return c # returning the sum of a and b to caller/main program
sum = add(1,2) # assigning function to a variable outside function
print(sum)


def add(a,b):
    return a + b
sum = add(1,2)
# Since function add returns, the return value can be further used in program outside function
print("The sum of two numbers is: ", sum)

# Two ways to assign function to a variable outside function
def add(a,b):
    return a + b
# First method to assign function to a variable
sum = add
print(sum) # this line prints the memory address of the function
print(sum(1,2)) # it prints the sum of a and b

# Second method to assign function to a variable
def add(a,b):
    return a + b
sum = add(1,2)
print(sum)
print("The sum of two numbers is: ", sum)


# Accepting user input from outside the function
first_num = int(input("Enter first number: "))
second_num = int(input("Enter second number: "))

def add(a, b): 
    return a + b
result = add(first_num, second_num)
print(result)
print(f"The sum of {first_num} and {second_num} is {result}")


# Using default parameter with user input in function
# if the user does not enter either first or second or both numbers, then 
# it is set to default value zero
first_num = int(input("Enter first number: ") or "0")
second_num = int(input("Enter second number: ") or "0")

def add(a, b):
    return a + b
result = add(first_num, second_num)
print(f"The sum of {first_num} and {second_num} is {result}")