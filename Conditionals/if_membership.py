"""YouTube Video Link: https://youtu.be/kwTLzVxaNWw"""


# Example of membership operators "in" and "not in"
s = "Hello World"

print("H" in s)
print("H" not in s)

l = [10,20,30]
print(33 in l)
print(33 not in l)


# Combining membership operator "in" with conditional if-else
colors = ["Red","Blue","Orange"]
user_color = input("Enter a color: ")

if user_color in colors:
    print(f"{user_color} in color list")
else:
    print(f"{user_color} not in color list")

# Combining membership operator "not in" with conditional if-else

colors = ["Red","Blue","Orange"]
user_color = input("Enter a color: ")
if user_color not in colors:
    print(f"{user_color} in not color list")
else:
    print(f"{user_color} in color list")

# Using membership operator "in" instead of "or" operator
user_name = input("Enter user name: ")
if user_name in ["root","admin","super user"]:
    print("Welcome Root/Admin")
elif user_name in ["test1","test2"]:
    print("Welcome Test User")
else:
    print("Unknown User")

# Using membership operator "in" instead of "and" operator

user_name = input("Enter name: ")
password = input("Enter password: ")

user_list = [("root","1234"),("admin","4321"),("super user","2345")]

if (user_name,password) in user_list:
    print(f"Hello, {user_name}")
else:
    print("Unknown User")

# Using membership operator "not in" instead of "or" operator

user_name = input("Enter name: ")
password = input("Enter password: ")

user_list = [("root","1234"),("admin","4321"),("super user","2345")]

if (user_name,password) not in user_list:
    print("Unknown User")
else:
    print(f"Hello, {user_name}")

# Using membership operator "not in" instead of "or" operator- futher simplification

user_name = input("Enter name: ")
password = input("Enter password: ")

if (user_name,password) not in [("root","1234"),("admin","4321"),("super user","2345")]:
    print("Unknown User")
else:
    print(f"Hello, {user_name}")