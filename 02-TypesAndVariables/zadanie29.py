import random

list = [1,2,3,4,5,6]
dice_first = random.choice(list)
dice_second = random.choice(list)
dice_third = random.choice(list)

print(f'First rolled dice: {dice_first}')
print(f'Second rolled dice: {dice_second}')
print(f'Third rolled dice: {dice_third}')
print(f'Sum of rolled dices: {dice_first+dice_second+dice_third}')
