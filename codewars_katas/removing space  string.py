arr='[2,4,6,2,10]'
def odd_one(arr):
    
    import ast
    a=ast.literal_eval(arr) 
    for i in a:
        if i%2!=0:
            return a.index(i)
        
    else:
        return -1
        
print(odd_one(arr))
