# YouTube Video Link: https://youtu.be/snZvX91CMv8

# Function returns addition and subtraction both in tuple form
def add_sub(a,b):
    return a + b, a - b
sum, diff = add_sub(5,2) # assigning return value to two variables
print(sum, type(sum))
print(diff, type(diff))
output = add_sub(5,2) # assigning return value to one variable
print(output, type(output))

# tuple unpacking
t = (10,20,30)
a, b, c = t
print(a)
print(b)
print(c)


# Function returns addition and subtraction both but in list form
def add_sub(a,b):
    return [a + b, a - b]
sum, diff = add_sub(5,2)
print(sum, type(sum))
print(diff, type(diff))
output = add_sub(5,2)
print(output, type(output))

# Returning 3 values but assigning to only two variables will result in error (ValueError)
def add_sub_multiply(a,b):
    return a + b, a - b, a * b
sum, diff = add_sub_multiply(5,2)
print(sum, type(sum))
print(diff, type(diff))
output = add_sub(5,2)
print(output, type(output))