# YouTube Video Link:https://youtu.be/JLhhsx8asPc

# Below code will accept only two arguments, nothing less or more
def add(a,b):
    return a + b
print(add(1,2))
# Below 2 lines will result in TypeError because the function add is defined
# with 2 parameters but is being called with NOT 2 argments.
# print(add(1)) 
# print(add(1,2,3))

# Using *args as parameters, you can call function with unlimited number
# of arguments.
def add(*nums):
    total = 0
    for num in nums:
        total = total + num
    return total
print(add())
print(add(1))
print(add(1,2))
print(add(1,2,3))

# *nums is nothing but tuple that collects all the arguments passed.
def add(*nums):
    print(type(nums))
    print(len(nums))
add(10,20,30,33,40)

# Tuple unpacking using *
t = 10,20,30,40
t1, *t2 = t
print("t1: ", t1)
print("t2: ", t2)

# Defining add function again but this type, accepting user input
numbers = []

while True:
    user_input = input("Enter number, Q to quit: ")
    if user_input.lower() == "q":
        break
    else:
        numbers.append(int(user_input))

def add(*args):
    return sum(args)
print(add(*numbers))


# positional parameter, default parameter and *args together
def total_order_cost(unit_price, quantity = 1, *delivery_fees):
    total_cost = unit_price * quantity + sum(delivery_fees)
    return f"Total Cost: {total_cost}"

print(total_order_cost(100))
print(total_order_cost(100, 3))
print(total_order_cost(100,3,2,10))