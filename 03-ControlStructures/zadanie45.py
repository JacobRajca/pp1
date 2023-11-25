number = int(input('Enter number which will be end of sequence: '))

i = 1
x = 1
new_string = ''

while i <= number:
    x = 2
    divide = 0
    if i > 1:
        while x <= i:
            if i%x==0:
                divide+=1
            x+=1
    if divide == 1:
        new_string = new_string + str(i) + ' '
    i+=1
print(f'{new_string}')