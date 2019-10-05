def strong_num(number):
    import math
    l=[]
    for i in str(number):
        l.append(math.factorial(int(i)))
        if sum(l)==number: return True
    else: return False      
print(strong_num(125))


