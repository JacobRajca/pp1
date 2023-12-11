import random
arr = []
for i in range(1,9):
    num = random.randrange(1,999)
    arr = arr + [num]
new_string = '|'

for element in arr:
    if element < 10:
        new_string = new_string + '   ' + str(element) + '|'
    elif element >= 10 and element < 100:
        new_string = new_string + '  ' + str(element) + '|'
    else:
        new_string = new_string + ' ' + str(element) + '|'

print('-----------------------------------------')
print(new_string)
print('-----------------------------------------')