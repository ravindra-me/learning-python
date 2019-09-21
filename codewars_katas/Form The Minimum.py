digits=[1, 3, 1]
def min_value(digits):
    return(int(''.join(str(i) for i in set(digits))))
print(min_value(digits))

