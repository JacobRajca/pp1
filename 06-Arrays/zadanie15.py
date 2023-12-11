arr = [[1,3,5],[8,7,2]]
print(f'{arr[0][0]+arr[1][2]}')
print(f'{arr[0][1]+arr[1][1]}')
i=0
sum=0
while i<len(arr[1]):
    sum = sum + arr[1][i]
    i+=1
print(sum)