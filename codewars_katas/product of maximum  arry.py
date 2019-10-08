lst=[10,8,7,9]
n=2
from functools import reduce
from operator import mul
from heapq import nlargest

def maxProduct (lst, n):
    return reduce(mul, nlargest(n, lst))
print(maxProduct(lst,n))