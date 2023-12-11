arr1 = [4,36,12,28,9,44,5] 
arr2 = [5,1,36]
arr3=[]
for element1 in arr1:
    num=0
    for element2 in arr2:
        if element1 != element2:
            num+=1
    if num == len(arr2):
        arr3 = arr3 + [element1]
print(arr3)