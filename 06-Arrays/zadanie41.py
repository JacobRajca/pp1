arr1 = [1,2,3,4,5,6,7,8]
arr2 = [9,123,41,51,124,63,8,7,6,5,4,3,2,1]
num = 0
for element1 in arr1:
    exist = False
    for element2 in arr2:
        if element1 == element2:
            exist = True
    if exist == True:
        num+=1

if len(arr1) == num:
    print('First array appear in second array')
else:
    print('Not all numbers from array first appear in second array')