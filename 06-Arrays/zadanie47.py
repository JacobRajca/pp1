arr = [
    [7,3,7,9,0],
    [2,9,0,1,5],
    [3,8,6,4,7],
    [8,7,1,1,5]
]
sum = 0
i = 0
while i < len(arr):
    j = 0
    while j < len(arr[i]):
        if i == len(arr)-1:
            sum+=arr[i][j]
        j+=1
    i+=1

print(sum)