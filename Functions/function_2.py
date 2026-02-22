# YouTube Video Link:https://youtu.be/_9C-TtcLv2U

# Positional Parameters. 
def subtract(a, b):
    print(a - b)

subtract(10,5) # 10 gets mapped to a and 5 gets mapped to b, resulting in 5
subtract(5,10) # 5 gets mapped to a and 10 gets mapped to b, resulting in -5


def country_capital(country, capital):
    print(f"{capital} is the capital of {country}.")

country_capital("India","New Delhi") # India gets mapped to country and New Delhi to capital
country_capital("New Delhi","India") # India gets mapped to country and New Delhi to capital


# Keyword Parameters
def subtract(a, b):
    print(a - b)

subtract(a = 10, b = 5)
subtract(b = 5, a = 10) # Order does not matter in Keyword arguments.

def country_capital(country, capital):
    print(f"{capital} is the capital of {country}.")

country_capital(capital = "New Delhi",country = "India")

def country_capital(country, capital):
    print(f"{capital} is the capital of {country}.")

# Positional arguments must come before keyword arguments.
country_capital("India", capital = "New Delhi")

def subtract(a, b):
    print(a - b)

subtract(10, b = 5)

# Function with positional, keyword and default argument all in one
def add(a, b , c = 1):
    print(a + b + c)
add(10,20,30)
add(10,20)
add(c=30, a= 10, b =20)

# While defining a function, non default parameter must be defined before default parameter
def add(a, c, b = 1):
    print(a + b + c)
add(10,20,30)