first = [0.2802, -0.1103, -0.2584, -0.0961, -0.4036, -0.3681, 0.4420, \
         0.4561, 0.0752, -0.4403, -0.2653, -0.1469, 0.3211, -0.4846, -0.4570, \
         -0.3311, 0.1491, 0.2317, 0.1477, -0.0491]
second =[]

sum = 0
for i in range(0,20):
    second.append(sum+first[i])
    sum = sum +first[i]
for i in range (0,int(20/5)):
    print('%9.4f%9.4f%9.4f%9.4f%9.4f'% (second[i],second[i+1],second[i+2],second[i+3], second[i+4]))
