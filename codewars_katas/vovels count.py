s="ravindra"
def count_vowels(s):
    vowel=['a','e','i','o','u','A','E','I','O','U']
    count=0
    for i in s:
        if i in vowel:
            count+=1
    return count
print(count_vowels(s))
    