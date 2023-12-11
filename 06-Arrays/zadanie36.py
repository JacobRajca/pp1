new_tuple = (50,20,40,50,30,50)
number = 50
i=0
sum=0
while i < len(new_tuple):
    if number == new_tuple[i]:
        sum+=1
    i+=1
print('Tuple:',end='')
for x in range(len(new_tuple)):
    print('% d' % new_tuple[x], end=' ')
print('')
print(f'Value: {number}')
print(f'Number of occurrences: {sum}')