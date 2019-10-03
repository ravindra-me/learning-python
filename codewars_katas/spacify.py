string = 'hello world'
def sapcify(string):
    result = ""
    for i in string:
        result += i+" "
    return result.rstrip()


print(sapcify(string))