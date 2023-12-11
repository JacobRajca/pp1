arr=[[0,0,0],[0,0,0],[0,0,0]]
i = 0
while i < len(arr):
    new_string=''
    j=0
    while j < len(arr[i]):
        if i==j:
            arr[i][j]=1
        if j==len(arr[i])-1:
            new_string = new_string + str(arr[i][j])
        else:
            new_string = new_string + str(arr[i][j])  + ' '
        j+=1
    print(new_string)
    i+=1