import ifinrange

x=int(input('Enter start of the range: '))
y=int(input('Enter end of the range: '))
check_number = ifinrange.within_range(x,y)
msg = f'Number 7 in the range <{x},{y}>: {check_number}'
print(msg)