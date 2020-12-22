
empty = []

response = 'y'
while (response.lower() == 'y'):
    from math import *
    m = float (input( 'Enter number in kilograms: '))
    k = float (input( 'Enter a stiffness in newtons/meters: '))
    c= float(input( 'Enter a damping in newtowns/(meter/second): '))
    Hz = (sqrt (k / m))/(2 * pi)
    t = c / (2 * (sqrt(k*m)))
    print ('Natural Frequency:', Hz , 'Hz')
    print ('Damping ratio:', t )
    if t == 0:
        system = 'undamped'
        print ('System Response: ', system)
    elif 0 < t < 1:
        system = 'underdamped'
        print ('System Response: ', system)
    elif t == 1:
        system = 'critically damped'
        print ('System Response: ', system)
    elif t > 1:
        system = 'overdamped'
        print ('System Response: ', system)
    response = input('Do another (y/n)?')
    more =[]
    more.append(m)
    more.append(k)
    more.append(c)
    more.append(Hz)
    more.append(t)
    more.append(system)
    empty.append(more)
print ('Summary:')
print('%10s%10s%15s%15s%15s' % ('Mass','Stiffness','Damping ', 'Omega_n Zeta ', 'Response Type'))
print('%10s%10s%15s%10s'%('kg', 'N/m','N/m(m/s)','Hz'))
print('%12s%12s%12s' % ('-'*30,'-'*30,'-'*30))
for n in empty:
    print('%10.4f%10.4f%12.4f%7.4f%9.4f%15s'%(n[0],n[1],n[2], n[3], n[4], n[5]))
       
