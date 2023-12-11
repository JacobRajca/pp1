arr = [[3,9,2],[2,4,5],[7,1,6],[0,4,8]]
sum=0
for row in arr:
    for element in row:
        if element%2!=0:
            sum = sum + element
print(sum)