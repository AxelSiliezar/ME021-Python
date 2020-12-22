import math
list00 = (0, 15, 45, 180, 210, 279)
#theta=0
#theta=15
#theta=45
#theta=180
#theta=210
#tetha=279
for theta in list00:
    numbers = theta*math.pi/180
    v = math.cos (-numbers)
    x = math.cos (numbers)
    y = math.tan (math.pi-numbers)
    z = -math.tan(numbers)
    print ("cos: for theta ", theta, 'LHS = ',(v),"RHS = ", (x))
    print ("tan: for theta ", theta, "LHS = ",(y),"RHS = ",(z))