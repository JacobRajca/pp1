university = 'Krakow University of Economics'

i=0
new_string = ''

while i < len(university):
    new_string = new_string + university[i] + ' '
    i+=1
print(f'{new_string}')