import mymath
import mykeyboard

num = mykeyboard.read_number()
random_number = mymath.generate_number()
print(f'Computer number: {random_number}')
if num == random_number:
    print(f'You won the game!!')
else:
    print(f'Maybe next time')