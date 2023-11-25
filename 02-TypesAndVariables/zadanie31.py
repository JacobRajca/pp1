import random

dice_rolled = random.randrange(1,6,1)
dice_guessed = int(input('Enter number from dice: '))

print(f'{dice_rolled == dice_guessed}')