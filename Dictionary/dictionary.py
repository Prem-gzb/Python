# create a dictionary
d1 = {1:"Simple",2:"Easy",3:"Python","pi":3.14}
print("d1 is of type: ", type(d1))
print("d1: ", d1)

# create a dictionary using dict constructor
d2 = dict([(1,"Simple"),(2,"Easy"),(3,"Python")])
print("d2 is of type: ", type(d2))

# # create an empty dictionary
d3 = {}
print("d3 is of type: ", type(d3))

# Using square brackets to find a value in the dictionary
# Will return KeyError if the key does not exist in the dictionary
print(d1["pi"])
print(d1[4])

# 1. get method same as square brackets but does not return any KeyError
# if key does not exist in the dictionary, instead returns None
print(d1.get(4)) # this code will return None

# # You can give a custom message instead of None in case Key is not in dictionary
print(d1.get(4,"Key Not Found")) # this code will return Key Not Found

# # Below code will print the value of pi since key pi exists in the dictionary
print(d1.get("pi","Key Not Found"))

# # Dictionary values can be updated using square brackets like below
print("d1 before update: ", d1)
d1[1] = "hello"
print("d1 after update: ", d1)

# 2. update Values can also be updated using update method.
# This is useful when multiple values are to be updated in one go.

d5 = {1:"Simple"}
print("d5 before update: " ,d5)
d5.update({2:"Easy",3:"Python"})
print("d5 after update: ", d5)

# 3. clear will remove all key value pairs and returns an empty dictionary
d1.clear()
print(d1)

# 4.copy creates a shallow copy
d6 = d1.copy()
print(d6)

# 5.fromkeys method takes keys from the dictionary and values from value given
# and creates a new dictionary. If no value is given, then None is used as value
print(dict.fromkeys(d1))
print(dict.fromkeys(d1,"Hello"))

# 6.items returns all the key value pairs in form of a set.
print(d1.items())

# 7.keys returns all the keys
print(d1.keys())

# 8.pop removes and returns the specified key's value
pop_element = d1.pop(2)
print(d1)
print(pop_element)

# 9.popitem removes and returns the last key value pair
pop_item = d1.popitem()
print(d1)
print(pop_item)

# 10.setdefault similar to get method but if the key being searched is NOT in
# the dictionary, it will insert it. If no value is specified, it will use
# None as default value
print(d1.setdefault(4,"Hello World"))
print(d1.setdefault(4))
print(d1)

# 11.values returns all the values of the dictionary
print(d1.values())






