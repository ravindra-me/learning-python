data = [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]
#def data_reverse(data):
b=" ".join(str (data[8:16]).replace('[','').replace(']',''))
c=" ".join(str (data[16:24]).replace('[','').replace(']',''))
d=" ".join(str(data[24:len(data)]).replace('[','').replace(']',''))
print(d,c,b,a)
