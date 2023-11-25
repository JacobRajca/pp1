def f(x,y):
    sum=0
    i=x
    while i<y:
        if i<0 and i%2==0:
            sum+=1
        i+=1
    return sum


print(f(-7,8))
print(f(-1,11))