"""The if, elif and else conditionals or control flow statement become
all the more powerful when used in combination with logical/Boolean and
comparison operators.
"""
# YouTube Video Link: https://youtu.be/1GryhVOzDic
# In this video, I have explained combining if, elif and else with logical 
# and operator.

# Example 1
# Combining logical and operator with if and else
user_name = input("Enter user name: ")
password = input("Enter password: ")

if user_name == "root" and password == "1234":
    print("Access Granted")
else:
    print("Invalid Credentials")

# Example 2
# Combining logical and operator with if, elif and else
user_name = input("Enter user name: ")
password = input("Enter password: ")

if user_name == "root" and password == "1234":
    print("Welcome root")
elif user_name == "user1" and password == "4321":
    print("Welcome User")
else:
    print("Unknown User")


