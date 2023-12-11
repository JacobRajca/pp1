array = [1,2,3,4,5]
print(array)
i = 0
while i < len(array):
    if i == 0:
        array[i] = array[i] - 1
        print(array)
    if i == len(array)-1:
        array[i] = array[i] + 4
        print(array)
    if i == len(array)//2:
        array[i] = array[i]*2
        print(array)
    i+=1