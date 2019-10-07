arr='[2,4,6,4,10]'
def odd_one(arr):
    import ast
    a=ast.literal_eval(arr) 
    for i in a:
        if i%2==0:
            pass
        else:
            return a.index(i)
print(odd_one(arr))
