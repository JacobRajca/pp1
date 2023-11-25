def f(x,y):
    sum = 0
    for i in range(x,y+1):
        print(i)
        if i%2==0 and i%3==0 and i%4!=0:
            sum = sum + i
    return sum

print(f(10,30))