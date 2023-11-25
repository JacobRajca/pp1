a = 4
b = 15
i = 1
x = 1
while i <= a:
    new_string = ''
    x=1
    while x <= b:
        if i == 1 or i == 4:
            new_string = new_string + '*'
            x+=1
        else:
            if x == 1 or x == 15:
                new_string = new_string + '*'
                x+=1
            else:
                new_string = new_string + ' '
                x+=1
    print(f'{new_string}')
    i+=1