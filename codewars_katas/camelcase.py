def gap(m,n):
    a=[]
    for i in range(m,n+1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            a.append(i)
    return(a)

print(gap(100,110))