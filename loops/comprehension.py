# YouTube Video Link: https://youtu.be/CH0owHcRiGI


# The traditional way to create squares of numbers from 1 to 3 using for loop
squares:list[int] = []

for i in range(1,4):
    squares.append(i ** 2)
print(squares)

# List Comprehension to create squares of numbers from 1 to 3 using for loop
squares:list[int] = [i ** 2 for i in range(1,4)]
print(squares)

# List Comprehension with list of strings
names:list[str] = ["Tom","Jared","SUSAN","TInA" ]
upper_case:list[str] = [name.upper() for name in names]
print(upper_case)

upper_case:list[str] = [name.upper() for name in ["Tom","Jared","SUSAN","TInA" ]]
print(upper_case)
lower_case:list[str] = [name.lower() for name in ["Tom","Jared","SUSAN","TInA" ]]
print(lower_case)

# Using for loop to create a list of Even Numbers from 1 to 10
even:list[int] = []
for i in range(1,11):
    if i % 2 == 0:
        even.append(i)
print(even)

# List Comprehension to produce even numbers from 1 to 10
# Using Conditional "if"
even:list[int] = [x for x in range(1,11) if x % 2 == 0]
print(even)

# Applying conditional "if" and "else" both to List Comprehension
x:list[str] = [f"{x} is even" if x % 2 == 0 else f"{x} is odd" for x in range(1,7)]
print(x)

# Applying conditional "if" with Boolean "and" in List Comprehension
x:list[int] = [x for x in range(1,16) if x % 2 == 0 and x % 3 == 0]
print(x)

# Applying conditional "if" with Boolean "and" and "or" in List Comprehension
x:list[int] = [x for x in range(1,16) if x % 2 == 0 or x % 3 == 0]
print(x)

# Nested for loop to produce the pairs
result = []
for x in range(3):
    for y in range(3):
        if x != y:
            result.append((x, y))
print(result)

# Nest List Comprehension to produce pairs
pairs = [(i, j) for i in range(3) for j in range(3) if i != j]
print(pairs)

# Set Comprehension
y:set[int] = {y ** 2 for y in range(3) }
print(y)

# Tuple Comprehension
t:tuple[int] = tuple(i ** 2 for i in range(3))
print(t)

# Generator Expression Generation using comprehension
x = (x ** 2 for x in range(5))
print(type(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
"""Now running this line 6th time will result in StopIteration Error because all the 
elements of the generator are already used."""
# print(next(x)) 