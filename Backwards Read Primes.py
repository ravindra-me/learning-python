def backwardsPrime(start, stop):
    l=[]
    for i in range(start,stop):
        if stop%i==0:
            pass
        else:
            l.append(i)
            l.reverse(i)
            return (list(l))

print(backwardsPrime(2,100))