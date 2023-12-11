with open('numbers.txt','r') as file:
    sum = 0
    new_string = ''
    for line in  file:
        sum += int(line.strip())
        new_string += line.strip() + ' '

print(sum)
print(new_string)