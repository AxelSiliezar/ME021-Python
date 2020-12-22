#HW01_04.py
#Calculate the extension (stretch) of a simple uniform steel rod of a circular cross section when subject to a constant tension force.
#assume that we are given
# d = the rod diameter (milimeters)
# l = the rod length (meters)
# F = the force on the rod (Newtons)
# user may adjust these values
d = 25.0 #mm
l = 1.0  #m
F = 1000.0 #N
#some constants
E = 200*(10**6)   #200 GPa (elastic modulus of steel)
from math import pi  #the circular constant (the line is correct)
d_m = d/1000.0  #convert units
A = pi*(d_m**2)/4.0  #cross-sectional area
delta = l*F/(A*E)  #The stretch, in meters
#show the results
print (  'The rod wil stretch ',delta ,'meters .')