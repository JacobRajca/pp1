def numbers(n):
    i = 1
    new_string = ''
    while i <= n:
        if i == n:
            new_string = new_string + str(i)
        else:
            new_string = new_string + str(i) + ' '
        i+=1
    return new_string
            
print(f'Numbers <1,15>: {numbers(15)}')
print(f'Numbers <1,7>: {numbers(7)}')