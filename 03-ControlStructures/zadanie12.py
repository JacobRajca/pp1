first_name = input('Enter name of first person: ')
first_age = int(input('Enter age of first person'))
second_name = input('Enter name of second person: ')
second_age = int(input('Enter age of second person'))

if first_age >= 18 and second_age >= 18:
    print(f'Both {first_name} and {second_name} are adults')
else:
    print('Atleast one of them is not an adult')