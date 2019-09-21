def findSmallestInt(arr):
    a=arr[0]
    for i in range(1,len(arr)):
        if arr[i]<a:
            a=arr[i]
    return a
print(findSmallestInt([1,2,4,8],9))