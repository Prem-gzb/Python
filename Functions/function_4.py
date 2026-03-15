# YouTube Video Link: https://youtu.be/yX_i5g-Yxrc

def add(a,b):
    print(a + b)
add(1,2) # this line outputs 3.
# Below line of code will produce 3 and  The sum of two numbers is: None
print("The sum of two numbers is: ", add(1,2))

# using return statement instead of print
def add(a,b):
    return (a + b)
output = add(1,2) #assigning the function to variable output
print(output)
# Below line will output The sum of two numbers is: 3
# showcasing that using return, we can use the return value further
# in program.
print("The sum of two numbers is: ", add(1,2))


# Multiple print statements in function.
def add(a,b):
    print(a + b)
    print("a :" , a)
    print("b: ", b)
add(1,2)

# Nothing gets executed after return statement
def add(a,b):
    return (a + b)
    print("a :" , a)# not going to be executed
    print("b: ", b) # not going to be executed
print(add(1,2))

# Multiple return statements but only one gets executed
def check_grade(marks):
    if marks > 80:
        return "Grade A"
    elif marks > 70:
        return "Grade B"
    elif marks > 60:
        return "Grade C"
    elif marks > 40:
        return "Grade D"
    else:
        return "Grade F"
marks = int(input("Enter marks: "))
print(check_grade(marks))

# return cannot be used outside function. Below code produces error.
a = 10
b = 20
return (a + b)