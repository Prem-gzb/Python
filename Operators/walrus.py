"""Walrus Operator: It is available in Pythonn 3.8 or higher.
Walrus operator is assignment expression operator.
Walrus operator allows you to assign, evaluate and return a value in a single line of code.
It is advised to put the walrus operator expression inside parentheses.
"""

# YouTube Video Link: https://youtu.be/rSKF9ntTMMM

a = 15 # It's an assignment statement. It assigns 15 to variable a.

10 - 2 # It's an expression which evaluates to some value, like 8 in this case and returns/prints it.

(a := 10) #It's a walrus operator which assigns the value 10 to a and returns it.

(b := 2 + 3) #It's a walrus operator which assigns the value 5 to a and returns it.
print(b) # Outputs 5. The walrus operator evaluates 2 +3 = 5 and assigns 5 to b.

"""Program to prompt the user to enter numbers and save them to a list as long as the user
enters a positive number. As soon as the user enters a negative number, the program quits 
and prints all the positive numbers entered so far.
"""

# Traditional Way
numbers = []

while True:
    num = int(input("Enter a number; enter negative number to quit: "))
    if num >= 0:
        numbers.append(num)
    else:
        break
        
print(numbers)


# Using Walrus Operator

numbers = []

while (num := int(input("Enter a number; enter negative number to quit: "))) >= 0:
    numbers.append(num)
    
print(numbers)