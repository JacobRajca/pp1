arr = [22,11,2,111,33,44,53,123,654,1234,564,342,75,63,346,234,745]
new_arr = []

for element in arr:
    if element%2==0:
        new_arr = new_arr + [element]

for element in arr:
    if element%2!=0:
        new_arr = new_arr + [element]

print(new_arr)