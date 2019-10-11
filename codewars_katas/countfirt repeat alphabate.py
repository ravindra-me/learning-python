s='a b c '
def first_dup(s):
    d = {}
    for i,val in enumerate(s):
        if s.count(val)>1:
            d[val] = s.count(val)
            return d[i]

        else:
            return None
print(first_dup(s))