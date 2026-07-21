# YouTube Video Link: https://youtu.be/TKjq2ROnN6Y

# lambda function without assigning to a variable
print((lambda x, y: x + y)(1,2))

# lambda function assigned to a variable
sum = lambda x, y: x + y
print(sum(1,2))

# lambda with if to find the greater of two numbers
a, b = 50, 5
max_num = lambda a, b: a if a > b else b
print(max_num(a,b))

# lambda with if and else to find the greatest of 3 numbers
a, b, c = 5, 15, 10
max_num = lambda a,b,c: a if (a > b and a > c) else (b if b > c else c)
print(max_num(a,b,c))

# lambda function to sort dictionary by value
phones = {"OnePlus": 799,"Apple": 1099, "Samsung":999, "Pixel":1199}
sort_by_price = sorted(phones.items(), key = lambda phones: phones[1])
print(sort_by_price)

# lambda function to sort dictionary by value in descending order
phones = {"OnePlus": 799,"Apple": 1099, "Samsung":999, "Pixel":1199}
sort_by_price = sorted(phones.items(), key = lambda phones: phones[1], reverse= True)
print(sort_by_price)

# Using lambda function with a Pandas DataFrame
import pandas as pd
data = {
    "Name":["Kate","Alice"],
    "Salary":[200_000, 50_000]
}
df = pd.DataFrame(data)
df["Tax"] = df["Salary"].apply(
    lambda salary: salary * 0.3 if salary > 100_000 else salary * 0.1
)
print(df)