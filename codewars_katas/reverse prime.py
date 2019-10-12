
def backwardsPrime(start, stop):
    l=[]
    for i in range(start,stop):
        for j in range(2,start):
            if i%j!=0:
                a=str(i)
                b=int(a[::-1])
                for z in range(2,b):
                    if b%z!=0:
                        l.append(i)
                        continue
    return l
print(backwardsPrime(9900,10000))
                        
                      