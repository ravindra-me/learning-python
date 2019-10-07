text=('wklv lv d vhfuhw phvvdjh')
def letter_frequency(text):
    s=text.replace(' ' ,'')
    return (sorted([(s.count(i),i)) for i in s],reverse=True))
   
print(letter_frequency(text))
