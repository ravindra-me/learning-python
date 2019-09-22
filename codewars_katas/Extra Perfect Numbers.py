n=28
def extra_perfect(n):
    l=[]
    for i in range(1,n+1):
        if i%2==0:
            pass
        else:
            l.append(i)
    
    return l
print(extra_perfect(n))