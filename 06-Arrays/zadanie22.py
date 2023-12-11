arr = [8,2,5,1,9]
i=0
while i < len(arr):
    arr[i] = arr[i]**2
    i+=1
print(arr)