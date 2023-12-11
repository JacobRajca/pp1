arr = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
i=0

while i < len(arr):
    j=0
    while j < len(arr):
        arr[i][j] = (i+1)*(j+1)
        print(arr[i][j],end=' ')
        j+=1
    print('')
    i+=1
