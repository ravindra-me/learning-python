num=4
a='a'
for i in range(1,num+1):
    for j in range(1,i+1):
        print(a,end=" ")
        a=chr(ord(a)+1)
    print()