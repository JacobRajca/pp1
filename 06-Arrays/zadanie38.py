number = int(input('Enter number: '))
arr = [12,23,8,1,20,55,142,99,33,959]
num=0
for element in arr:
    if number < element:
        num +=1

print(f'Amount of numbers in array greater than number entered: {num}')