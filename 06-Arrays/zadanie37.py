import MyArrays as arrays

new_array = [7,3,8,5,2]

i=0
new_string = ''
while i < len(new_array):
    if i == len(new_array)-1:
        new_string = new_string + str(new_array[i])
    else:
        new_string = new_string + str(new_array[i]) + ','
    i+=1

print(f'Numbers: {new_string}')
print('Second largest number: ', end='')
print(arrays.a([7,3,8,5,2]))
print('Difference between largest and lowest number: ', end='')
print(arrays.b([7,3,8,5,2]))
print('Median: ', end='')
print(arrays.c([7,3,8,5,2]))
y = arrays.d([7,3,8,5,2])
print('Smallest and largest numbers: ', end='')
for i in range(len(y)):
    print('% d' %y[i], end=' ')
print('')
print('Numbers as a string: ', end='')
print(arrays.e([7,3,8,5,2]))