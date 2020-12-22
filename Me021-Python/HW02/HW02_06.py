#Repeat
response = "y"
while (response[0].lower()=="y"):
    import math
    Ang_1 = float(input ("Enter value for angle: ")) #value in degrees
    Ang_2 = float(input ("Enter value for angle: ")) #value in degrees
    ang_1 = Ang_1*(math.pi/180) #convert to radians
    ang_2 = Ang_2*(math.pi/180) #convert to radians
    cos1 = math.cos(ang_1)
    cos2 = math.cos(ang_2)
    if (cos1 > cos2):
        print (cos1,Ang_1)
    elif (cos1 < cos2):
       print (cos2,Ang_2)
    else:
        print ("Both angles are the same") 
    response = input ('Do another (y/n) ?')