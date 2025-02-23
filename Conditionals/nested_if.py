"""YouTube Video Link: https://youtu.be/Ag6DwG6wfN0"""

user_name = input("Enter user name: ")
password = input("Enter password: ")

# First example of one level of nesting if under first if condition

if user_name == "root":
    if password == "1234":
        print("Access Granted")
    else:
        print("Incorrect password")
else:
    print("Unauthorised User")


# Second example. The if is nested in first if condition and else part.
if user_name == "root":
    if password == "1234":
        print("Access Granted")
    else:
        print("Incorrect password")
else:
    if user_name == "user1":
        if password == "4321":
            print("Welcome User")
        else:
            print("Incorrect Password, try again !!!")


# Third example. The if is nested in first if condition, inside the elif also and in else part.
if user_name == "root":
    if password == "1234":
        print("Access Granted")
    else:
        print("Incorrect password")
elif user_name == "user1":
    if password == "4321":
        print("Welcome User")
    else:
        print("Incorrect Password, try again !!!")
else:
    print("Unauthorised User")

