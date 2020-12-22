import math
#given
M = input ("Enter value for M: ")
M = float(M) 
m = input ("Enter value for m: ")
m = float (m)
r = input ("Enter value for r: ")
r = float (r)
G = 6.674*10**(-11)  #Nm^2/kg^2
 #G = universal gravitational constant
F = ((G)*(M*m/r**2))
print ("The value of F is: ",(F))


