import random

dice_rolled = random.randrange(1,6,1)
print(f'Dice rolled: {dice_rolled}')
print(f'Special nuimber: {dice_rolled == 1 or dice_rolled == 6}')