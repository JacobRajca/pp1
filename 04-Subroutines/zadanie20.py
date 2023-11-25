import mykeyboard

number = int(input('Enter number: '))
num1 = mykeyboard.read_number()
msg = f'{number} + {num1} = {number+num1}'
print(msg)