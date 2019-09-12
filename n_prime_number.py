n=int(input("enter the number"))
x=2
l=[]
while n5:
    for i in range(2,x):
        if x%i==0:
            break
    else:
        l.append(x)
        n=n-1
    x=x+1
print(set(l))
            
