# YouTube video link: https://youtu.be/zaX3PIPeTHg

"""and operator
It will evalate to True if both the expression on left side and right side of and are True otherwise False
"""
# Below is the truth table for and operator
print(True and True) # evaluates to True
print(True and False) # evaluates to False
print(False and True) # evaluates to False
print(False and False) # evaluates to False

"""or operator
It will evaluate to True of either of the expression on left side and right side of or is True. If both expressions
on left and right of or are false, then it will evaluate to False.
Both and and or are binary in nature because they need to two expressions (one on left and another on right) to
evaluate.
"""
# Below is the truth table for or operator
print(True or True) # evaluates to True
print(True or False) # evaluates to True
print(False or True) # evaluates to True
print(False or False) # evaluates to False

"""not operator
not operator is prefixed to a Boolean value and reverses its result. Unlike and and or, it takes only one expression
so is unary in nature.
"""

print(not True) #evaluates to False
print(not False) # evaluates to True
print(not not not True) # evaluates to False

"""Priority of evaluation
First not is evaluated, then and and finally or is evaluated.
not and or
"""

# Combining comparison operators with Boolean operator
print(10 < 20 and 20 < 30) # evaluates to True
print(10 < 20 and 20 > 30) # evaluates to False

print(10 < 20 or 20 > 30) # evaluates to True

"""Bonus Tip 1
True = 1 and False = 0
"""

l1 = [1,2,3,True]
l2 = [1,2,3, False]
print(sum(l1)) # outputs 7
print(sum(l2)) # outputs 6

"""Bonus tip 2
0 = False
Non-zeros are True
"""
print(bool(0)) # outputs False
print(bool(255)) # outputs True