def f(number):
    i = 0
    x= str(number)
    sum = 0
    while i < len(x):
        j = i+1
        while j < len(x):
            if x[i] == x[j]:
                print('Similar number')
                sum = sum + int(x[i])
            j+=1
        i+=1
    return sum

print(f(513553007))