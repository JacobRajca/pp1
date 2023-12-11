arr = ['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy']
long_name = ''
for element in arr:
    if len(long_name) < len(element):
        long_name = element
print(long_name)