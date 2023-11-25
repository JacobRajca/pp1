new_string = ''

for i in range (1,31):
    if i%3==0:
        if i%5==0:
            new_string = new_string +'BINGO' + ' '
        else:
            new_string = new_string +'THREE' + ' '
    elif i%5==0:
        if i%3==0:
            new_string = new_string +'BINGO' + ' '
        else:
            new_string = new_string +'FIVE' + ' '
    else:
        new_string = new_string + str(i) + ' '

print(f'{new_string}')