d = {'a' : 1, 'b' :2}
print (d)
d['a'] = 100
d['c'] = 3
d['d'] = 4
print (d)
clas ={}
response = 'y'
while (response.lower() == 'y'):
    name = input('Enter a name:' )
    score = input ('Enter a score:' )
    clas[name] = score
    response = input ('Enter more data (y/n)?')
print (clas)
       

