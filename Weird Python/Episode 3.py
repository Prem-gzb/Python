# YouTube Link: https://youtu.be/gvmrQUdUQjQ


text = "I love Python"

# Output is Jave Found
if text.find("Java"):
    print("Java Found")
else:
    print("Java not found")


""" Explanation
find method returns -1 if given string is not found. In Python, 0 is False while non-zero is True. 
If you try bool(text.find("C++")), it is equivalent to bool(-1) which is True. 
Thus, the if statement is Truthy and it prints Java Found
"""