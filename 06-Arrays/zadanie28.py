def check(x,y):
    if len(x) == len(y):
        i=0
        num=0
        while i <len(x):
            if x[i]==y[i]:
                num+=1
            i+=1
        if num == len(x):
            msg = 'Arrays are equal'
        else:
            msg = 'Arrays are different'
    else:
        msg = 'Arrays are different'
    return msg

arr1 = ["water","book","sky"]
arr2 = ["water","book","sky"]
arr3 = [True,False]
arr4 = [True,False,True]
arr5 = [5,3,1]
arr6 = [5,3,1]
arr7 = [3,2,1]
arr8 = [3,2]

print(check(arr1,arr2))
print(check(arr3,arr4))
print(check(arr5,arr6))
print(check(arr7,arr8))