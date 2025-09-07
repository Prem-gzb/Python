# YouTube Video Link: https://youtu.be/G6E8D5wV3Nw

my_list = enumerate(["Simple","Easy","Python","Hello","World"])
print(my_list)
print(list(my_list))

my_list = enumerate(["Simple","Easy","Python","Hello","World"])
print(next(my_list))
print(next(my_list))
print(next(my_list))
print(next(my_list))
print(next(my_list))
# this line will show StopIteration Error becuase all the elements of enumerate object 
# are printed and nothing more is left.
print(next(my_list))

# Custom Enumerate Program using built in Enumerate function. 
# It will print index starting with zero.
my_list = enumerate(["Simple","Easy","Python","Hello","World"])

while True:
    try:
        index, value = next(my_list)
        print(index, value)
    except StopIteration:
        break

# Custom Enumerate Program using built in Enumerate function.
# It will print index starting with input given by the user.
start_index = int(input("Enter the start index: ") or 0)
my_list = enumerate(["Simple","Easy","Python","Hello","World"], start = start_index)

while True:
    try:
        index, value = next(my_list)
        print(index, value)
    except StopIteration:
        break

# Custom Enumerate Program, not using the built in Enumerate function. 
# It will print index starting with zero in case user does not specify 
# else will start from user input.
my_list = ["Simple","Easy","Python","Hello","World"]

def my_enumerate(iterable, start = 0):
    index = start
    for item in iterable:
        yield index, item
        index += 1

# Below code will print index from 0.
for i, v in my_enumerate(my_list):
    print(i, v)

# Below code will start index from user specified value, -10 in this case.
for i, v in my_enumerate(my_list, start = -10):
    print(i, v)