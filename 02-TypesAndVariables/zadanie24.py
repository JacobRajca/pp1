str1 = 'KR'
str2 = 'KK'
registration_number = input('Enter vehicle registration number: ')
if str1 in registration_number or str2 in registration_number:
    print('Car from Kraków: True')
else:
    print('Car from Kraków: False')