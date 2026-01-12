# YouTube Video Link: https://youtu.be/RR7YL9HpkCs

d:dict[int:int] = {}

for i in range(1,4):
    d[i] = i ** 2
print(d)

d:dict[int:int] = {i: i ** 2 for i in range(1,4)}
print(d)
phones:dict[str, float] = {"OnePlus": 799,"Apple": 1099, "Samsung":999, "Pixel":1199}
for k, v in phones.items():
    phones[k] = v * 0.9
print(phones)

phones:dict[str, float] = {k:v * 0.9 for k, v in phones.items()}
print(phones)
phones:dict[str, float] = {"OnePlus": 799,"Apple": 1099, "Samsung":999, "Pixel":1199}
new_prices:dict[str, float] = {k:v * 0.9 for k, v in phones.items()}
print(phones)
print(new_prices)
phones:dict[str, float] = {"OnePlus": 799,"Apple": 1099, "Samsung":999, "Pixel":1199}
phones:dict[str, float] = {k: v * 0.9 for k, v in phones.items() if v > 1000}
phones:dict[str, float] = {k: (v * 0.9 if v > 1000 else v) for k, v in phones.items()}
print(phones)
new_phones:dict[str, float] = {k: (v * 0.9 if v > 1000 else v) for k, v in phones.items()}
print(new_phones)
capital:list[str] = ["Paris","New Delhi","Madrid"]
country:list[str] = ["France","India","Spain"]
output:dict[str:str] = dict(zip(capital,country))
print(output)
output:dict[str:str] = {k:v for k, v in zip(capital, country)}
print(output)