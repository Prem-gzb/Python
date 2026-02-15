# YouTube Video Link: https://youtu.be/AiHUtaI9HQs

"""All user defined functions must start with keyword def, the function name must start with
a letter or underscore. 
Defining a function is not enough. In order for a function to work it must be called.
All code related to the function must be indented. Any code outside the indentation does belong
to the function.
"""

# Defining a very basic function

def first_func():
    print("Hello World")
    print("Python")
print("It was my first function")
# Below code calls the function, named first_func
first_func()
# Below code will print the memory address of the function
print(first_func)

# Accepting an input via the function

def first_func():
    print("Hello, ", input("What's your name? "))
first_func()


# Function with parameter where the input is passed while calling the function.
def func_with_parameter(name):
    print("Hello, ", name)
func_with_parameter("Kate")

# Two parameter defined, so two argument need to be passed while calling the function.

def func_with_parameter(f_name, l_name):
    print("Hello, ", f_name, l_name)
func_with_parameter("Kate","Perry")

# Function with default parameter. The default parameter comes into play when argument is not passed while
# calling the function otherwise argument passed when calling overrides it.

def func_with_parameter(name = "Guest"):
    print("Hello, ", name)
func_with_parameter("Kate")
func_with_parameter()

# Function with default parameter

def add(a, b = 1):
    print(a + b)

add(2, 3)
add(2)





