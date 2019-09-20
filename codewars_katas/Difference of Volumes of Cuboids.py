def find_difference(a, b):
    m=1
    n=1
    for i in a:
        m=m*i
    for j in b:
        n=n*j
    return(m-n)
print(find_difference([3, 2, 5], [1, 4, 4]))