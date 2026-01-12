# YouTube Video Link: https://youtu.be/RR7YL9HpkCs

# Tradition way of using for loop to create a dictionary from range

d:dict[int:int] = {}

for i in range(1,4):
    d[i] = i ** 2
print(d)

# Dictionary Comprehension to create dictionary from a range
d:dict[int:int] = {i: i ** 2 for i in range(1,4)}
print(d)

# Using for loop to change the values in existing dictionary
phones:dict[str, float] = {"OnePlus": 799,"Apple": 1099, "Samsung":999, "Pixel":1199}
for k, v in phones.items():
    phones[k] = v * 0.9
print(phones)

# Changing the values in existing dictionary using dictionary comprehension
phones:dict[str, float] = {k:v * 0.9 for k, v in phones.items()}
print(phones)

# Changing the values in new dictionary using dictionary comprehension
phones:dict[str, float] = {"OnePlus": 799,"Apple": 1099, "Samsung":999, "Pixel":1199}
new_prices:dict[str, float] = {k:v * 0.9 for k, v in phones.items()}
print(phones)
print(new_prices)

# Using conditional "if" to modify value if price is more than 1000
phones:dict[str, float] = {"OnePlus": 799,"Apple": 1099, "Samsung":999, "Pixel":1199}
phones:dict[str, float] = {k: v * 0.9 for k, v in phones.items() if v > 1000}

# Using conditional "if" and "else" to modify value if price is more than 1000
# so that dictionary still has values as it is if price is less than 1000
# but reduced price if price is more than 1000
phones:dict[str, float] = {k: (v * 0.9 if v > 1000 else v) for k, v in phones.items()}
print(phones)


new_phones:dict[str, float] = {k: (v * 0.9 if v > 1000 else v) for k, v in phones.items()}
print(new_phones)

# Using zip to iterate through two lists and creating a dictionary
capital:list[str] = ["Paris","New Delhi","Madrid"]
country:list[str] = ["France","India","Spain"]
output:dict[str:str] = dict(zip(capital,country))
print(output)

# Using dictionary comprehension to iterate through two lists and creating a dictionary
output:dict[str:str] = {k:v for k, v in zip(capital, country)}
print(output)