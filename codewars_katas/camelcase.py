'''
Write simple .camelCase method (camel_case function in PHP, CamelCase in C# or camelCase in Java) for strings. 
All words must have their first letter capitalized without spaces.
'''
string = 'test case'


def camel_case(string):
    return ''.join(i.title() for i in string.split(' '))

print(camel_case(string))

