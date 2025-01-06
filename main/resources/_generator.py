import sys

lst = [i for i in range(1, 100001)]
print(f"Size of the list : {sys.getsizeof(lst)}")

g = (i for i in range(1, 100001))
print(f"Size of the generateor : {sys.getsizeof(g)}")
