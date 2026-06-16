# YouTube Video Link: https://youtu.be/E03i_2fAHUE

def calculate_bill(*args, **kwargs):
    total = sum(args)
    discount = kwargs.get("discount", 0)
    total -= total * (discount /100)
    tax = kwargs.get("tax", 0)
    total += total * (tax /100)

    return total 
print(calculate_bill(100,200, discount = 10, tax = 5))
print(calculate_bill(100,200, discount = 10))
print(calculate_bill(100,200, tax = 5))
print(calculate_bill(discount = 10, tax = 5))
print(calculate_bill())

help(print)