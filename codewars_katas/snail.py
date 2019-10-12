array=[[1,2,3],
         [4,5,6],
         [7,8,9]]
def snail(array):
    out = []
    while len(array):
        out += array.pop(0)
        array = list(zip(*array))[::-1] # Rotate
    return out
print(snail(array))