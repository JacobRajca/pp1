decimal_number = int(input('Enter decimal number: '))
x = decimal_number
i = 1
binary_number = ''

while i <= x:
    if x%2==0:
        binary_number = '0' + binary_number
    else:
        binary_number = '1' + binary_number
    x = int(x/2)
print(f'{decimal_number} (10) = {binary_number} (2)')