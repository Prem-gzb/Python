# # Defining a set using curly braces {}
s1 = {1,2,3,1,"Simple","Easy","Python"}

# # Defining set using set constructor
s2 = set({1,2,3,1,"Simple","Easy","Python"})
s3 = set([1,2,3,1,"Simple","Easy","Python"])

print("s1 is: ", type(s1))
print("s2 is: ", type(s2))
print("s3 is: ", type(s3))


# # Defining a single element set
s4 = {1}
print("s4 is: ", type(s4))

# # Defining an empty set
s5 = {} # It will create an empty dictionary and not an empty set
print("s5 is: ", type(s5))
 
# Below line of code will create an empty set
s6 = set()
print("s6 is: ", type(s6))

# printing a set
s1 = {1,2,3,1,"Simple","Easy","Python"}
print(s1)

# add method
s1 = {1,2,3,1,"Simple","Easy","Python"}
s1.add(6)
print(s1)

# copy method, creates a shallow of the set.
s_copy = s1.copy()
print(s1)
print(s_copy)

# discard method. If the element is not part of the set, remove method will not 
# throw any error. It will simply return the set as it is.
s1 = {1,2,3,1,"Simple","Easy","Python"}
s1.discard(30)
print(s1)

# pop method. It will remove an arbitrary element and return it.
s1_pop = s1.pop()
print(s1)
print(s1_pop)

# remove method. If element is no part of the set, remove will throw KeyError.
s1 = {1,2,3,1,"Simple","Easy","Python"}
s1.remove(22)
print(s1)

# update method. Same like add, updates the set with the new element.
s1 = {1,2,3,1}
s2 = set({1,2,3,1,"Simple","Easy","Python"})
s1.update(s2)
print(s1)

# clear method. Removes all elements from the set, returning a null or empty set.
s1.clear()
print(s1)

# I have created three new sets for below methods, just to have a real world example.
python = {"John","Susan","Linda","Peter"}
c = {"Linda","Rose","Peter","Tim","Audrey"}
java = {"Elon","Bill","Jelan","Peter"}

# Union => returns a new set with elements who are either part of python,
# or part of c or part of both the sets. You may pass more than one set in parentheses
python_c = python.union(c, java)

# Pipe operator is same as union in line 72
python_c = python | c
print(python_c)

# Intersection => returns a new set with elements which are common or present in
# both the sets.
python_c = python.intersection(c)

# & (ampersand) operator same intersection in as line 80
python_c = python & c
print(python_c)

# Intersection update => same as intersection method but does not return a new set
# instead makes changes in the set named first
print("Before intersection: ", python)
python.intersection_update(c)
print("After intersection: ",python)



# Difference => returns a new set with elements which are in first set (python here)
# but not in second set(c here)
diff = python.difference(c)
diff = c.difference(python)

# - or minus operator same as difference in line 96 or 97
diff = python - c
print(diff)

# difference_update => same difference method but does not return a new set,
# instead makes changes in the first set named(python here)
print("Python set before difference update: ", python)
python.difference_update(c)
print("Python set after difference update: ", python)

# symmetric_difference => it returns a new set with elements which are in first
# set only (python here) and in second set (c here) only and removes common elements
# from these two sets.

# diff = python.difference(c)
# diff = python.difference(c)
# print(diff)
diff = python.symmetric_difference(c)

# ^ or caret operator same as symmetric_difference in line 144
diff = python ^ c
print(diff)

# symmetric_difference_update => same as symmetric_difference but does not reutrn 
# a new set. Instead makes changes in set name first(python here)
python.symmetric_difference_update(c)
print(python)











