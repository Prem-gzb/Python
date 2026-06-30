# YouTube Video Link:https://youtu.be/9sPfZsuw0lQ

# First example with *args and **kwargs
def calculate_bill(*args, **kwargs):
    total = sum(args)
    discount = kwargs.get("discount", 0)
    total -= total * (discount /100)
    tax = kwargs.get("tax", 0)
    total += total * (tax /100)

    return total 
# Example usage
print(calculate_bill(100,200, discount = 10, tax = 5))
print(calculate_bill(100,200, discount = 10))
print(calculate_bill(100,200, tax = 5))
print(calculate_bill(discount = 10, tax = 5))
print(calculate_bill())

# Second Example with *args and named keyword and **kwargs
def calculate_bill(*args, default_tax=5, delivery_charge=50, **kwargs):
    total = sum(args)

    discount = kwargs.get("discount", 0)
    total -= total * (discount / 100)

    tax = kwargs.get("tax", default_tax)
    total += total * (tax / 100)

    if not kwargs.get("free_delivery", False):
        total += delivery_charge

    return f"Total Bill = {total}"
# Example usage
print(calculate_bill(100, 200, 50))                        # Uses default tax=5, delivery=50
print(calculate_bill(500, discount=10, default_tax=8))     # Override default tax to 8%
print(calculate_bill(100, 200, tax=12, free_delivery=True))# Custom tax, no delivery fee
print(calculate_bill())                                    # this will output 50 although no items in shopping cart

# Third Example with *args and named keyword and **kwargs and ensuring zero amount if shopping cart is empty
def calculate_bill(*args, default_tax=5, delivery_charge=50, **kwargs):
    total = sum(args)

    discount = kwargs.get("discount", 0)
    total -= total * (discount / 100)

    tax = kwargs.get("tax", default_tax)
    total += total * (tax / 100)

    if args and not kwargs.get("free_delivery", False):
        total += delivery_charge

    return f"Total Bill = {total}"
# Example usage
print(calculate_bill(100, 200, 50))                        # Uses default tax=5, delivery=50
print(calculate_bill(500, discount=10, default_tax=8))     # Override default tax to 8%
print(calculate_bill(100, 200, tax=12, free_delivery=True))# Custom tax, no delivery fee
print(calculate_bill())                                    # this will output now zero when no items in shopping cart


# Fourth and final example with positional, default, *args, named keyword and **kwargs
def calculate_bill(cust_name, order_id, membership = "Regular",/,
        *args,default_tax = 10, delivery_charge = 50,
                    **kwargs):
    print(f"Customer Name: {cust_name}")
    print(f"Order Number: {order_id}")
    print(f"Membership Type: {membership}")

    total = sum(args)
    discount = kwargs.get("discount", 0)
    total -= total * (discount / 100)
    tax = kwargs.get("tax", default_tax)
    total += total * (tax / 100)
    if args and not kwargs.get("free_delivery", False):
        total += delivery_charge
    return f"Total Bill = {total}"
print(calculate_bill("Kate",1001,"Gold", 500, 30)) # positional(Kate and 1001), overrides default membership,*args (500, 30), default tax and delivery charges
print(calculate_bill("Kate",1001, "Regular",500, 30)) # positional(Kate and 1001), default membership, *args (500, 30),tax and delivery charges
print(calculate_bill("Kate",1001,"Gold", 500, discount = 10, default_tax = 8)) # positional(Kate and 1001), overrides default membership, *args (500), overrides default tax and delivery charges added
print(calculate_bill("Kate",1001,"Gold", 100, 200, default_tax = 12, free_delivery = True)) # positional(Kate and 1001), overrides default membership, *args(100, 200), overrides default tax and delivery waived