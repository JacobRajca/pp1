arr = [[-38, 19],[5,40],[-7,11],[29,16]]
min_ele = min(arr[0])
max_ele = max(arr[0])
i =0
while i < len(arr):
    j = 0
    while j < len(arr[i]):
        if min_ele >= arr[i][j]:
            min_ele = arr[i][j]
            min_loc = []
            min_loc += [i]
            min_loc += [j]
        if max_ele <= arr[i][j]:
            max_ele = arr[i][j]
            max_loc = []
            max_loc += [i]
            max_loc += [j]
        j+=1
    i+=1

print(f'Max number : {max_ele}')
print(f'Max location: {max_loc}')
print(f'Min number : {min_ele}')
print(f'Min location: {min_loc}')