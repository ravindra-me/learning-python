arr=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
def count_positives_sum_negatives(arr):
    l=[]
    a=[]
    c=[]
    for i in arr:
        if i>=0:
            l.append(i)
        elif i<=0:
            a.append(i)
    return (c.append(sum(l),c.append(sum(a)))
print(count_positives_sum_negatives(arr))