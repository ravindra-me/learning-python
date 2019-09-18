
s= ''
def is_palindrome(s):
    a=s.lower()
    while a:
        if a==a[::-1]:
            return True 
        else:
            return False

    # if s.lower() == s.lower()[::-1]:
    #     return True
    # else:
    #     return False
print(is_palindrome(s))       
        
    