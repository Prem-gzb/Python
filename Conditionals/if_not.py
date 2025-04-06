"""YouTube Video Link: https://youtu.be/beCMlX5vsS4"""

print(5)
print(bool(5))
print(not 5)

# Check if the list is empty
l = []  
print(bool(l)) # outputs False
print(not l) # outputs True


l = [1,2,3,"Python"]
print(bool(l)) # outputs True
print(not l) #outputs False

# Combining not with if else
# below code will output List is empty
l = [] 
if not l:
    print("List is empty")
else:
    print("List is not empty")

# below code will output List is not empty
l = [1,2,3,"Python"] 
if not l:
    print("List is empty")
else:
    print("List is not empty")

# Combining not with membership operator
num_range = range(1,11)
print(5 in num_range) #outputs True
print(15 in num_range) #outputs False
print(15 not in num_range) #outputs True

# Combining not with membership operator and if else
num_range = range(1,11)
num = int(input("Enter a number: "))

if num not in num_range:
    print("Number of out of range")
else:
    print("Number within the range")

# Combining if else with logical and operator
error_code = 404

if not (error_code > 400 and error_code < 404):
    print("Unauthorized/Payment Required/Forbidden")
else:
    print("Page Not Found")
