i = 1
x = 1
while i <= 9:
    new_string = ''
    x=1
    while x <= i:
        new_string = new_string + str(i)
        x+=1
    print(f'{new_string}')
    i+=1