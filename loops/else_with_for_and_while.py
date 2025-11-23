# YouTube Video Link: https://youtu.be/jrPxXITBasQ

# else with for loop in number range - normal termination
for i in range(1,10,3):
    print(i)
else:
    print("Loop Over")

# else with for loop in list - normal termination
my_list = ["Python","C","C++"]

for i in my_list:
    print(i)
else:
    print("Loop Over")

# else with while loop - normal termination
i = 1

while i < 10:
    print(i)
    i += 3
else:
    print("Loop Over")

# else with for loop - with break statement
for i in range(1,10,3):
    if i == 7:
        break
    print(i)
else:
    print("Loop Over")


# else with for loop - with break statement
for i in range(3):
    password = input("Enter password: ")

    if password == "1234":
        print("Hello User, Access Granted")
        break
else:
    print("You have exceeded maximum number of attempts, Account Locked")


# else with while loop - with break statement
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    password = input("Enter Password: ")
    if password == "1234":
        print("Hello User, Access Granted.")
        break
    attempts += 1
else:
    print("You have exceeded maximum number of attempts, Account Locked")