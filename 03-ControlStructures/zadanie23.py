dogs_age = int(input('Enter the dog age in the human years: '))

sum = 0
i = 1

while i <= dogs_age:
    if i == 1 or i == 2:
        sum+= 10.5
    else:
        sum+= 4
    i+=1

print(f'The dogs age in dogs years is {int(sum)} years.')