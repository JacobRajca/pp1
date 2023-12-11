arr = [[2,5,4],[9,0,3]]
print(arr)
print(f'{len(arr)} | {len(arr[0])}')
print(arr[0][1])
print(arr[1][2])
i=0
new_string = ''
while i < len(arr[1]):
    if i == len(arr[1])-1:
        new_string = new_string + str(arr[1][i])
    else:
        new_string = new_string + str(arr[1][i]) + ' '
    i+=1
print(new_string)
    