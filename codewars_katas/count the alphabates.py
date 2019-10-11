string="ravindrasingh"
def count(string):
    res={i:string.count(i) for i in set(string)}
    return res 
    if string=='':
        return {}
print(count(string))