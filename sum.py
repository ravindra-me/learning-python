letters=['a', 'b', 'c']
def add_letters(letters):
    # a=list(*letters)
    # return(str(chr(ord(a[-1])+1)))
    letters.append(chr(ord(letters[-1])+1))
    return letters
print(add_letters(letters))
