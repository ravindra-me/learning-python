chars=['a','b','c','d','f']
def find_missing_letter(chars):
    for i in chars:
        if chr(ord(i)+1) in chars:
            pass
        else:
            return str(chr(ord(i)+1))
    
print(find_missing_letter(chars))
