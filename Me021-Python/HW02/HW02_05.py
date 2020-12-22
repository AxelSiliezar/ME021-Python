#Collect values
MAXVAL = range (100+1)
user = int(input('Enter a number between 1 - 10: '))
for value in HW:
    if (value%user == 0):
        print(value)