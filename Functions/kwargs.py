# YouTube Video Link:https://youtu.be/XWqW06WMqig

def func(**shopping_list):
    print(type(shopping_list))
    print(shopping_list)

func(Shirts = 2, Shoes = 3)
func(Shirts = 2, Shoes = 3, Tie = 1)

# Using **kwargs, you can accept unlimited number of keyword arguments.
def func(**kwargs):
    for k, v in kwargs.items():
        print(f"{k} = {v}")

func(Shirts = 2, Shoes = 3)
func(Shirts = 2, Shoes = 3, Tie = 1)

# Using **kwargs with named/normal keyword parameter
def func(Tie = 2, **kwargs):
    print(f"Tie = {Tie}")
    for k, v in kwargs.items():
        print(f"{k} = {v}")

func(Shirts = 2, Shoes = 3)
func(Shirts = 2, Shoes = 3, Watch = 5)