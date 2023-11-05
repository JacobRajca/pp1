first_number = int(input('Enter first number: '))
second_number = int(input('Enter second number: '))

if first_number >= 0 or second_number >= 0:
    print(f'At least one of entered numbers {first_number} and {second_number} is not negative')
else:
    print(f'Both numbers {first_number} and {second_number} are negative')