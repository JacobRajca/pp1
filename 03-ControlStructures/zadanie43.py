i = 1
x = 0
y = 1
new_string = '0 1 '
while i <= 20:
    if i >= 3:
        b = x + y
        x = y
        y = b
        new_string = new_string + str(b) + ' '
    i+=1
print(f'{new_string}')