def f(number,even):
    x = str(number)
    i=0
    sum = 0
    y = 0
    while i < len(x):
        y = int(x[i])
        if even == True:
            if y%2==0:
                sum = sum + y
        if even == False:
            if y%2!=0:
                sum = sum + y
        i+=1
    return sum

if __name__ == '__main__':
    print(f(3124,True))
    print(f(3124,False))
    print(f(20576,False))
    print(f(20576,True))
    print(f(13115,True))