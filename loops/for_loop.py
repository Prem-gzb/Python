# YouTube Video Link: https://youtu.be/_MeDce4uGK4

# Looping through list
my_list = ["Simple","Easy","Python","Hello","World"]

for i in my_list:
    print(i)

# Replacing the variable my_list and directly using the list in a for loop
for i in ["Simple","Easy","Python","Hello","World"]:
    print(i)

# Looping through strings
my_str = "Python"

for i in my_str:
    print(i)

# Replacing the variable my_str and directly using the list in a for loop
for i in "Python":
    print(i)

# Looping through a list of integers
nums = [10,20,30]
for n in nums:
    print(n, end = " ")

# Looping through a number range, starting with 0
r = range(5)
for i in r:
    print(i)

# Looping through a number range from 5 till 10
for i in range(5,11):
    print(i)

# Looping through number range from 5 to 0 in descending order
for i in range(5,0, -1):
    print(i)

# Looping through the indices of a list
for i in range(len(["Simple","Easy","Python","Hello","World"])):
    print(i)

# Looping through the indices and values of a list
my_list = ["Simple","Easy","Python","Hello","World"]

for i in range(len(my_list)):
    print(i, my_list[i])

# Looping through a number for indices and values
my_range = range(10,16)

for i in range(len(my_range)):
    print(i, my_range[i])

# Nested for loop
for i in range(3):
    for j in range(10,13):
        print(i, j)