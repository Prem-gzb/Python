# YouTube Link: https://youtu.be/7qtzHYE4fYk

# Python Official Document link:
# https://docs.python.org/3/library/stdtypes.html#truth-value-testing
# Below program outputs 3 is the largest number. No brainer.
if 3 > 2 > 1:
    print("3 is the largest number")
else:
    print("3 is not the largest number")

# Same as above, below program outputs 3 is the largest number
if (3 > 2) > -1:
    print("3 is the largest number")
else:
    print("3 is not the largest number")

# Below program outputs 3 is not the largest number. In Python, True is 1 and False is 0.
# Therefore, (3 > 2) is True and below code can be rewritten as
# True > 1
# Now True can be replaced with 1 and it becomes
# 1 > 1 which is not True because 1 is equal to 1 and not greater than 1
# Therefore, below code outputs 3 is not the largest number

if (3 > 2) > 1:
    print("3 is the largest number")
else:
    print("3 is not the largest number")

