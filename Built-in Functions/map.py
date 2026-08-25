# YouTube Video Link:https://youtu.be/tIGtXGS8xU8

# Traditional way to multipy each number of a list by 2
def double(lst):
    new_lst = []
    for i in lst:
        new_lst.append(i * 2)
    return new_lst
l = [10,20,30]
print(double(l))

# Multipy each number of a list using Map function
def double(x):
    return x * 2
l = [10,20,30]
print(list(map(double, l)))

# Map when used without converting output to list produces map object
def double(x):
    return x * 2
l = [10,20,30]
new_lst = map(double, l) 
print(new_lst) # it will produce map object of type iterator
print(next(new_lst))
print(next(new_lst))
print(next(new_lst))
# print(next(new_lst)) # this line will output StopIteration Error

# Map with in built function len
lst = ["India","USA","Australia"]
print(list(map(len,lst)))

# Map with lambda that multiplies each number of list by 2
lst = [10,20,30]
new_lst = list(map(lambda x: x * 2, lst))
print(new_lst)

# Map with multiple iterables
def add(x,y):
    return x + y
lst_1 = [10,20,30]
lst_2 = [1,2,3]
print(list(map(add, lst_1, lst_2)))

def calculate_bill(customer_name, 
order_id,
membership="Regular"):
    total = 1000
    tax = total * 0.05
    return total + tax