# YouTube Video Link: https://youtu.be/X6VK9sruLE4

# Loop through dictionary

phones:dict[str, float] = {"OnePlus": 799,"Apple": 1099, "Samsung":999, "Pixel":1199}

for k in phones:
    print(k)

# Loop through dictionary keys
phones:dict[str, float] = {"OnePlus": 799,"Apple": 1099, "Samsung":999, "Pixel":1199}
for k in phones.keys():
    print(k)

# Loop through dictionary values
phones:dict[str, float] = {"OnePlus": 799,"Apple": 1099, "Samsung":999, "Pixel":1199}
for v in phones.values():
    print(v)


# Loop through dictionary key and values
phones:dict[str, float] = {"OnePlus": 799,"Apple": 1099, "Samsung":999, "Pixel":1199}
print(phones.items())
for k, v in phones.items():
    print(k, v)

# Looping through dictionary key in ascending order
phones:dict[str, float] = {"OnePlus": 799,"Apple": 1099, "Samsung":999, "Pixel":1199}
for k in sorted(phones):
    print(k, phones[k])

# Looping through dictionary key in ascending order
phones:dict[str, float] = {"OnePlus": 799,"Apple": 1099, "Samsung":999, "Pixel":1199}
for k in sorted(phones, reverse = True):
    print(k, phones[k])

# Looping through dictionary values in ascending order
phones:dict[str, float] = {"OnePlus": 799,"Apple": 1099, "Samsung":999, "Pixel":1199}
for k, v in sorted(phones.items(), key = lambda item: item[1]):
    print(k, v)
print(phones.items())

# Looping through dictionary values in descending order
phones:dict[str, float] = {"OnePlus": 799,"Apple": 1099, "Samsung":999, "Pixel":1199}
for k, v in sorted(phones.items(), key = lambda item: item[1], reverse = True):
    print(k, v)
print(phones.items())

# Modifying value in place while looping
phones:dict[str, float] = {"OnePlus": 799,"Apple": 1099, "Samsung":999, "Pixel":1199}
for k, v in phones.items():
    if v > 1000:
        phones[k] = v * 0.9
print(phones)

# Modifying value in new dictionary while looping
phones:dict[str, float] = {"OnePlus": 799,"Apple": 1099, "Samsung":999, "Pixel":1199}
new_prices:dict[str, float] = {}

for k, v in phones.items():
    if v > 1000:
        new_prices[k] = v * 0.9
print(new_prices)
print(phones)
        