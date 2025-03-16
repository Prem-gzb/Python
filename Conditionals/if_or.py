'''YouTube Video Link: https://youtu.be/wuICmJu0TtI'''

user_name = input("Enter user name: ")

if user_name == "root" or user_name == "admin" or user_name == "super user":
    print("Welcome Root/Admin")
else:
    print("Unknown User")


'''Instead of "or", one can use if, elif and else construct also.
But normally, if, elif and else construct is normally used when the course of action
is different in various conditions. If the course of action is same, it is advisable
to use "or", like in below example where we are printing the same message in if and elif.
It makes code compact, concise and readable.
'''
if user_name == "root":
    print("Welcome root/admin")
elif user_name == "admin":
    print("Welcome root/admin")
elif user_name == "super user":
    print("Welcome root/admin")
else:
    print("Unknown User")