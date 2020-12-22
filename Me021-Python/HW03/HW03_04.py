fighter = int(input('Choose your character: ')) #Only valid from 1-12
if (fighter >= 12):
    print ('Please try again with a number between 1-11')
else:
    ClassNum = { 1: 'barbarian', 2 : 'bard', 3: 'cleric', 4: 'figther', 5: 'monk', 6: 'paladin', 7: 'ranger', 8: 'rogue', 9: 'sorcerer', 10: 'wizard', 11: 'aberration'}   
    print ('The character you have selected corresponds to %s.'
       % (ClassNum [fighter]))