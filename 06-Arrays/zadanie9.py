array =[2,3,7,5,4]
print(array)
print(len(array))
print(array[0])
print(array[1])
print(array[-1])
print(array[len(array)-1])
print(array[len(array)//2])
i=0
new_string=''
while i < len(array):
    if i == len(array)-1:
        new_string = str(array[i])
    else:
        new_string = str(array[i]) + ' '
    i+=1
print(new_string)