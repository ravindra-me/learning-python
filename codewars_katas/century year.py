def century(year):
    if year%100==0:
        return (year//100)
    else:
        return (1+year//100)
print(century(1973))    