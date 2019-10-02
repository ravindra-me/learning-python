l=[]
for i in range(10,20)
    for j in range(n+1):
        if i%j==0:
            break
    else:
        l.append(i)
print(l)
