haystack=(['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False], 3)
def find_needle(haystack):
    for i in haystack:
        return i.index('needle')
print(find_needle(haystack))