# You Tube Video Link:
# "https://youtu.be/mFwaQfgGuGQ"

# Methods are of two types.
# Methods used below like upper() and type() are built in ones
var = "Hello World"
print("var is: ", var)
print(var.upper())

l = [10,5,2,-6,4]
print("l is of type : ", type(l))
l.sort()
print(l.upper()) #this line of code will run into error because
# there is upper() method associated with lists.

# sum and diff defined below are examples of user defined mehtods
class addition:
    def __init__(self, value_1, value_2):
        self.value_1 = value_1
        self.value_2 = value_2

    def sum(self):
        return self.value_1 + self.value_2
obj_1 =addition(2,3)
print(obj_1.sum())

class difference:
    def __init__(self, value_1, value_2):
        self.value_1 = value_1
        self.value_2 = value_2

    def diff(self):
        return self.value_1 - self.value_2
obj_2 = difference(2,3)
print(obj_2.diff())

# A method is always bound to an object.
# A method bound with one object may or may not work with 
# another object. diff is bound to obj_1 and does not work
# with obj_2 and throws an error.
obj_1.diff(2,3)

# Functions are also of two types, built in and user defined
# print() is built in function.
# A function may or my not return anything.
# In below example, print() does not return anything and
# prints nothing on the screen.
print()

# below functions are user defined functions.
# A function may or may not accept an argument.

def foo():
    print("Hello World")
foo()

# below defined function takes an argument.
# If I put 3 in parantheses while calling it, it is going to
# print Hello World that many times.
def foo(n):
    print("Hello World" * n)
foo(3)
