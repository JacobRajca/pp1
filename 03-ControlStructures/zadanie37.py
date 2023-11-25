amount_of_rows = int(input('Enter number of rows: '))

i = 1
x = 1
y = 0
new_string = ''

if amount_of_rows%2==1:
    highest_point = int(amount_of_rows/2) + 1
    while i <= amount_of_rows:
        new_string = ''
        if i <= highest_point:
            y=y+1
        else:
            y=y-1
        x=1
        while x <= y:
            new_string = new_string + '*'
            x+=1
        print(f'{new_string}')
        i+=1
else:
    highest_point = int(amount_of_rows/2)
    while i <= amount_of_rows:
        new_string = ''
        if i <= highest_point:
            y=y+1
        elif i == highest_point+1:
            y=y
        else:
            y=y-1
        x=1
        while x <= y:
            new_string = new_string + '*'
            x+=1
        print(f'{new_string}')
        i+=1