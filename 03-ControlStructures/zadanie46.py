i = 1
j = 1
while i <= 7:
    new_string = ''
    x = 1
    while x <= 49:
        if (x-i)%7==0:
            new_string = new_string + str(x) +  ' '
        x+=1
    print(f'{new_string}')
    i+=1