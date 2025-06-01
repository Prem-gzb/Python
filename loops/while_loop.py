# YouTube Video Link: https://youtu.be/g09wRWUOlb8


# Looping through a list
my_list = ["Simple","Easy","Python", 3.14]

condition = 0
while condition < len(my_list):
    print(my_list[condition])
    condition += 1

# Looping through number ranges
i = 0

while i < 5:
    print(i)
    i += 1

# Looping through number range with step value
i = 10

while i < 50:
    print(i)
    i += 5

# Looping through number range in descending order
i = 50

while i > 10:
    print(i)
    i -= 5

# Creating an infinte loop that will run forever till the time user does not 
# enter a specific input
response = [1,2,3]
choice = 0
while choice not in response:
    print("1. Withdraw money")
    print("2. Check balance")
    print("3. Quit")
    choice = int(input("Enter your choice (1, 2 or 3): "))
if choice == 1:
    print("Withdrawing money")
elif choice == 2:
    print("Checking balance")
elif choice == 3:
    print("Thank you for using our services")
