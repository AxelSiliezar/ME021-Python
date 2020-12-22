ans = 'y'
UserVals = []
while (ans.lower() != 'q'):
    UserVals.append(float(input('Enter a value: ')))
    ans = input('Enter Q to quit or anything else to continue: ')
from math import *
if (floor(UserVals[0])==UserVals[0]):
    FormatStr = 'The values entered were: %3d'
else:
    FormatStr = 'The values entered were: %5.2f'

if ( len(UserVals) > 1) :
    for val in UserVals[1:-1]:
        if (floor(val) == val):
            FormatStr = FormatStr + ', %3d'
        else:
            FormatStr = FormatStr + ', %5.2f'
        
    if (floor(UserVals[-1]) == UserVals[-1]):
        FormatStr = FormatStr + ', and %3d.'
    else:
        FormatStr = FormatStr + ', and %5.2f.'
        
else: # only one value entered
        FormatStr = FormatStr + '.'
print(FormatStr % tuple(UserVals))


