Rollerbearing = 'CylindricalRollerBearingData_01.txt'
startp = []
endresults = []
with open(Rollerbearing, 'r') as Fulldata:
    next(Fulldata)
    next(Fulldata)
    headers = Fulldata.readline().split('\t')

    for H in range(len(headers)):
        startp.append([])
    for line in Fulldata:
        y = line.split('\t')
        for f in range(len(headers)):
            startp[f].append(y[f])
    for R in range(len(startp) - 1):
        for L in range(len(startp[R])):
            startp[R][L] = float(startp[R][L])
listmax = []
listmin = []
newmax = []
newmin = []

for i in range(len(startp) - 1):
    newmin.append(min(startp[i]))
    listmin.append(min(startp[i]))
    newmax.append(max(startp[i]))
    listmax.append(max(startp[i]))
String = '%20s' * len(headers[0:-1]) \
         % tuple(headers[0:-1])
String1 = '%20s' * len(listmin) \
          % tuple(listmin)
String2 = '%20s' * len(listmax) \
          % tuple(listmax)
print('Current limits are:')
print('    ' + String)
print('min' + String1)
print('max' + String2)
count = 0
with open(Rollerbearing, 'r') as Fulldata:
    next(Fulldata)
    next(Fulldata)
    next(Fulldata)
    for count, line in enumerate(Fulldata):
        count += 1

verify = True
while True:
    while verify:
        endresults = []
        print('There are currently', count, 'rows of data within these limits.')
        limits = str(input('Do you want to alter the limits (Y/N)? '))

        if limits.lower() == 'y':
            for i in range(len(listmin)):
                print('%5s' % headers[i], 'must be between', '%.2f' % listmin[i], 'and', '%s' % listmax[i])
                minv = input('     Enter new upper limit or [Enter] to keep %.2f: ' % newmin[i])
                if minv != '':
                    newmin[i] = float(minv)
                maxv = input('     Enter new upper limit or [Enter] to keep %.2f: ' % newmax[i])
                if maxv != '':
                    newmax[i] = float(maxv)
            String = '%20s' * len(headers[0:-1]) \
                     % tuple(headers[0:-1])
            String1 = '%20s' * len(newmin) \
                      % tuple(newmin)
            String2 = '%20s' * len(newmax) \
                      % tuple(newmax)
            print('Current limits are: ')
            print('    ' + String)
            print('min' + String1)
            print('max' + String2)
        for i in range(len(startp[0])):
            rowAdd = True
            for k in range(len(startp) - 1):
                if not ((startp[k][i] >= newmin[k]) and (startp[k][i] <= newmax[k])):
                    rowAdd = False
            if rowAdd:
                temp = []
                for k in range(len(startp)):
                    temp.append(startp[k][i])
                endresults.append(temp)
        count = len(endresults)
        if limits.lower() == 'n':
            break

    verify = False
    print("Data within chosen limits:")
    lastheaders = '%22s' * (len(headers)) \
                  % (tuple(headers))
    print(lastheaders)
    for k in endresults:
        for i in k:
            i = str(i)
        last = '%22s' * (len(k)) \
               % (tuple(k))
        print(last)

    laststring = str(input('"Y" to do another one, anything else to quit:'))
    if laststring.lower() == 'y':
        print('Current limits are: ')
        print('    ' + String)
        print('min' + String1)
        print('max' + String2)
        verify = True
    else:
        break
