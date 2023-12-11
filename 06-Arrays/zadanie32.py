def occurs(number,array):
    n = len(array)
    present = False
    for element in array:
        if number == element:
            present = True
    if present == True:
        msg = f'Result: number {number} appears in the array'
    else:
        msg = f'Result: number {number} does not appear in the array'
    return msg
arr = [15, 38, 7, 23, 14]
number = int(input('Enter number to be checked in array: '))
print(f'Number: {number}')
print('Array:', end='')
for i in range(len(arr)):
    print(' % d' % arr[i], end = ' ')
print('')
print(occurs(number,arr))
    