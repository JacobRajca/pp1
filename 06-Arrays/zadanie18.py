arr = [[True,False],[True,True],[False,False]]
i = 0
while i < len(arr):
    j =0
    while j <len(arr[i]):
        if arr[i][j]==True:
            arr[i][j]=False
        else:
            arr[i][j]=True
        j+=1
    i+=1
print(arr)