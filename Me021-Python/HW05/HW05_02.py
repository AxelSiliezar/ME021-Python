Myfile=open('HW05_02_SpringData.txt','r')
file_out=open('HW05_02_out.txt','w')

file_out.write('Spring Test Data, February, 2020\n')
print('Spring Test Data, February, 2020')
file_out.write ('%10s%15s%15s' % ('weight', 'displacement','stiffness\n'))
print('%10s%15s%15s' % ('weight', 'displacement','stiffness'))
file_out.write ( '%10s%15s%15s' %  ('(N)','(mm)','(N/m)\n'))
print( '%10s%15s%15s' %  ('(N)','(mm)','(N/m)'))
file_out.write ('%7s%16s%15s' % ('---------','-----------','---------\n'))
print('%7s%16s%15s' % ('---------','-----------','--'*4))
with open('HW05_02_SpringData.txt','r') as MyOpenFile:
    p = MyOpenFile.readline()
    p = MyOpenFile.readline()
    p = MyOpenFile.readline()
    p = MyOpenFile.readline()
    for line in MyOpenFile:
        x = line.rstrip().split()
        k = (float(x[0]) / float(x[1]))
        print('%10.3f%14.3f%15.3f' % (float(x[0]) , float(x[1]), k))
        file_out.write('%10.3f%14.3f%15.3f\n' % (float(x[0]) , float(x[1]), k))
        #k = (float(x[0]) / float(x[1]))
        
        #print('%40.3f%40.3f%40.3f' % (x[0],x[1],k))
#print('%10.3f%14.3f' % (float(x[0]) , float(x[1])))
            
       
        
#k= x[0]/x[1]
#for stif in MyOpenFile:
#    stif = MyOpenFile[1] / MyOpenFile [2]
#file_out = ('HW05_02_SpringData.txt', 'w')
file_out.close()
