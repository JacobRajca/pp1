arr = [2,3,2,5,8,1,9,8]
i=0
arr_unique = []
while i < len(arr):
    j=0
    unique = True
    while j < len(arr):
        if i != j:
            if arr[i] == arr[j]:
                unique = False
        j+=1
    if unique == True:
        arr_unique = arr_unique + [arr[i]]
    i+=1

print('Array:')
for x in range(len(arr)):
    print("% d" % arr[x], end=" ")
print('')
print('Unique elements:')
for y in range(len(arr_unique)):
    print("% d" % arr_unique[y], end=" ")