# Membership Operators
# YouTube video link: https://youtu.be/-mLoW9hk6jQ
"""
There are two membership operators, in and not in
These operators check if the given element is present or not in the sequence like
string, list, tuple, set and dictionary and prints Boolean True or False.
in operator checks if the element is present and if yes, outputs True else False
not in operator checks if the element is not present and if yes, outputs True else False
"""
s1 = "Hello World"
s2 = "12345"
l = [10,20,30,40]
t = (10,20,30,40)
s = {10,20,30,40}
d = {"a":10, "b":20, "c":30, "d":40}

# in operator
print("H" in s1) #outputs True
print(10 in l) #outputs True
print(11 in l) #outputs True
print(10 in t) #outputs True
print(10 in s) #outputs True

# not in operator
print("H" not in s1) #outputs False
print(10 not in l) #outputs False
print(11 not in l) #outputs False
print(10 not in t) #outputs False
print(10 not in s) #outputs False

"""checking if the key is present in dictionary"""
print("a" in d.keys()) #outputs True
print("a" not in d.keys()) #outputs False
print(d["a"]) #outputs value associated with key a if key is present in the dictionary
print(d["x"]) #outputs KeyError if key is not present in dictionary
# with get method, if the key is present in dictionary, you can give a custom message.
print(d.get("x","Key Not Present"))

"""checking if the value is present in the dictionary"""
print(10 in d.values()) #outputs True
print(10 not in d.values()) #outputs False
print(50 not in d.values()) #outputs True


