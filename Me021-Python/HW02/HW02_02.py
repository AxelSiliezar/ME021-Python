#Assign each fighter a number
fighter = int(input('Choose your character: '))
if (fighter == 0):               
    fighter = 'barbarian'
elif (fighter ==1):               
    fighter = 'bard'
elif (fighter ==2):               
    fighter = 'cleric'
elif (fighter ==3):               
    fighter = 'druid'
elif (fighter ==4):               
    fighter = 'fighter'
elif (fighter ==5):               
    fighter = 'monk'
elif (fighter ==6):               
    fighter = 'paladin'
elif (fighter ==7):               
    fighter = 'ranger'
elif (fighter ==8):               
    fighter = 'rogue'
elif (fighter ==9):               
    fighter = 'sorcerer'    
elif (fighter ==10):               
    fighter = 'wizard'
elif (fighter ==11):               
    fighter = 'aberration'    
else:
    fighter='Error'

print ('The character you have selected: ', fighter)







