digits=[1,5,1]
def min_value(digits):
    l = list(set(digits))
   
    return sorted(sum(x * 10**i for i, x in enumerate(l)))
print(min_value(digits))