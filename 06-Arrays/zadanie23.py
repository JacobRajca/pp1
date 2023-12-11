arr = [-15, 8, -31, 47, -2, 19]
min=0
max=0
for element in arr:
    if element < min:
        min = element
    if element > max:
        max = element
print(f'min: {min} | max: {max}')