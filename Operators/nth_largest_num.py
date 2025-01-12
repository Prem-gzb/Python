"""
There are multiple ways to find second or third largest or smallest number in a list, tuple or set.
I have discussed three ways in this video, first one using sort method which works only with lists while
the other two, using sorted function and heapq library works with lists, tuples or sets.

YouTube Video Link: https://youtu.be/nc4-g-D-Zr8
"""

l = [10,20,-12,-9,44]
import random, timeit, heapq

lst = []

for i in range(100_000):
    lst.append(random.randint(-100, 100_000))

def max_min():
    print("Largest number is: ", max(lst))
    print("Smallest number is: ", min(lst))

def func1():
    t1 = timeit.timeit()
    lst.sort()
    print("Largest Number is: ", lst[-1])
    print("Second largest number is: ", lst[-2])
    print("Smallest number is: ", lst[0])
    print("Second Smallest number is: ", lst[1])
    print("Time taken by sort method is: ", t1)
    print()

def func2():
    t2 = timeit.timeit()
    print("Largest Number is: ", sorted(lst)[-1])
    print("Second Largest Number is: ", sorted(lst)[-2])
    print("Smallest Number is: ", sorted(lst)[0])
    print("Second smallest Number is: ", sorted(lst)[1])
    print("Time taken by sorted function is: ", t2)
    print()

def func3():
    t3 = timeit.timeit()
    print("Three largest numbers are: ", heapq.nlargest(3, lst))
    print("Three smallest numbers are: ", heapq.nsmallest(3, lst))
    print("Time taken by heapq is: ", t3)

# max_min()
func1()
func2()
func3()