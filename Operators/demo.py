import random, timeit, heapq

lst = []

for i in range(100_000):
    lst.append(random.randint(-100,100_000))

def func1():
    print("Function 1 Running ....")
    t1 = timeit.timeit()
    lst_sorted = sorted(lst)
    print(lst_sorted[-2])
    print("Time taken by sorted function: ", t1)
    print()
    
def func2():
    print("Function 2 Running ....")
    t2 = timeit.timeit()
    lst.sort()
    print(lst[-2])
    print("Time taken by sort method: ", t2)
    print()

def func3():
    print("Function 3 Running ....")
    t3 = timeit.timeit()
    second_largest = heapq.nlargest(2,lst)
    print(second_largest)
    print("Time taken using heapq: ", t3)

func1()
func2()
func3()




# a = 0.1 + 0.3
# b = 0.4
# print(a == b)

# x = 0.1 + 0.2
# y = 0.3
# print(x == y)