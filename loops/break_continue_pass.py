#  YouTube Video Link: https://youtu.be/ELwH0TXMAEY

# pass
for i in range(5):
    pass
    print(i)

# continue in for loop
for i in range(5):
    if i == 2:
        continue
    print(i)

# continue in while loop
i = 0
while i < 5:
    i += 1
    if i == 2:
        continue
    print(i)

# break in for loop
for i in range(5):
    if i == 2:
        break
    print(i)

# break in for loop skipping else part
for i in range(5):
    if i == 2:
        break
    else:
        print(f"i is not 2, therefore, printing {i}")

# break in while loop
i = 0
while i < 5:
    if i == 2:
        break
    print(i)
    i += 1

# break in nested for loop
for i in range(3):
    for j in range(10,16):
        if j == 12:
            break
        print(f"i = {i}, j = {j}")

# Avoiding zero division error using continue and break
while True:
    num = int(input("Enter numerator: "))
    den = int(input("Enter denominator: "))

    if den == 0:
        continue
    else:
        print(f"{num} / {den} = {num/den}")
        break