arr1=[1, 2, 3, 4]
arr2=[5, 6, 7, 8]
def merge_arrays(arr1, arr2):
    return sorted(set(arr1+arr2))
print(merge_arrays(arr1,arr2))