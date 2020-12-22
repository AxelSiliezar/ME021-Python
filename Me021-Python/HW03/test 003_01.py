#Part A
list = [-3, 0 , 3, 6]
print ('%3d%3d%3d%3d' % (list[0] , list[1], list[2] , list[3]))
#Part B
empty = []
full = [1 , 2, 3, 4]
for news in full:
    empty.append((news-2)*3)

print ('%5d %5d %5d %5d' % (empty[0], empty[1], empty [2], empty [3]))
#Part C
elmnts = []
response = "yes"
while (response.lower()=="yes"):
        elmnts.append (int(input("enter value:")))
        response = input ('Do you want another one (yes/no)?')
print (elmnts)
#Part D
rev = (elmnts[:])
rev.sorted (reverse=True)
print (rev) 
