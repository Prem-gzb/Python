# Difference between sort and sorted
# YouTube video link: https://youtu.be/dSqLLYZdMXc

s = "SimpleEasyPython"
l = [10,2,22,3,0,-7,15,8]
t = (10,2,22,3,0,-7,15,8)

# sort() is a Python list method, it makes sorts the list inplace
# and does not return anything.
l.sort()
print(l)

t.sort()#t is tuple and hence sort() cannot be applied to it.
# If applied, it throws error.

# sort() cannot be applied on Python string and tuple.
# sorted() is a function that can be applied on Python
# string, list and tuple. It returns a new sorted list.
s_new = sorted(s)
l_new = sorted(l)
t_new = sorted(t)

print(s_new)
print(l_new)
print(t_new)