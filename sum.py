letters=['a', 'b', 'c']
def add_letters(*letters):
    a=list(*letters)
    return(str(chr(ord(a[-1])+1)))
print(add_letters(letters))
