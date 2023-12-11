def convert_array(x):
    arr = []
    for row in x:
        for element in row:
           arr+=[element]
    return arr

array1 = [[2,3],[1,5]]
array2 = [[5,0,3,7,5],[9,0,9,1,2]]
array3 = [[2,1],[3,5],[7,4],[2,6]]

result1 = convert_array(array1)
result2 = convert_array(array2)
result3 = convert_array(array3)

for element in result1:
    print(element,end=' ')
print('')
for element in result2:
    print(element,end=' ')
print('')
for element in result3:
    print(element,end=' ')
print('')