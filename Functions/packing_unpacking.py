# YouTube Video Link:https://youtu.be/Bxd5y8y8sC8

# Packing
lst = [10,20,30] # Packing elements to a list
t = 11,12,13 # Packing elements to a tuple
my_dict = {"A":20,"B":21,"C":"Carol"} # Packing elements to a dictionary


# Unpacking a list
l1, l2, l3 = lst
print("lst:", lst, type(lst))
print("l1:", l1, type(l1))
print("l2:", l2, type(21))
print("l3:", l3, type(l3))


# Unpacking a tuple
t1, t2, t3 = t
print("t:", t, type(t))
print("t1:", t1, type(t1))
print("t2:", t2, type(t2))
print("t3:", t3, type(3))


# Unpacking dictionary keys
k1, k2, k3 = my_dict.keys()
print(k1)
print(k2)
print(k3)

# Unpacking dictionary values
v1, v2, v3 = my_dict.values()
print(v1)
print(v2)
print(v3)

# Extended unpacking a list using single asterisk
lst = [10,20,30,40,50]
l1, *l2, l3 = lst
print("lst:", lst, type(lst))
print("l1:", l1, type(l1))
print("l2:", l2, type(l2))
print("l3:", l3, type(l3))


lst = [10,20,30,40,50]
*l1, l2= lst
print("lst:", lst, type(lst))
print("l1:", l1, type(l1))
print("l2:", l2, type(l2))
# print("l3:", l3, type(l3))

# Extended Unpacking tuple using single asterisk
t = 11, 12,13, 14
t1, *t2 = t
print(t1, type(t1))
print(t2, type(t2))


# Extended unpacking dictionary keys and values
my_dict = {"A":20,"B":21,"C":"Carol"}
k = [*my_dict]
print(k)
v = [*my_dict.values()]
print(v)

# Ignoring values while extended unpacking
lst = [10,20,30,40,50]
l1, *_l2, l3 = lst
print("lst:", lst, type(lst))
print("l1:", l1, type(l1))
# print("l2:", l2, type(l2))
print("l3:", l3, type(l3))

# Merging multiple lists
lst1 = [10,20]
lst2 = ["Sam","Carol",3.14]
new_lst = [*lst1, *lst2]
print(new_lst)

# Merging multiple dictionaries
d1 = {"a":1,"b":2}
d2 = {"x":5,"y":"Carol", "z":3.14}
d = {**d1, **d2}
print(d)

# Swapping two values
a = 5
b = 10
a, b = b, a
print(a)
print(b)

# Using single asterisk or *args to unpack function variable length non-keyword paramert
def add(*nums):
    return sum(nums)
print(add(1,2))
print(add(1,2, 3))

# Using double asterisks or *kwargs to unpack function variable length keyword paramert
def item_details(**kwargs):
    print(type(kwargs))
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(f"{key}: {value}")
item_details(Item = "Coke", Quantity = 6)
item_details(Item = "Coke", Quantity = 6, Type = "Soda")