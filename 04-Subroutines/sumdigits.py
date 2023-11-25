def f(number,even):
    i=0
    num_str = str(number)
    sum=0
    while i < len(num_str):
        if even == True and int(num_str[i])%2==0:
            sum = sum + int(num_str[i])
            i+=1
        elif even == False and int(num_str[i])%2!=0:
            sum = sum + int(num_str[i])
            i+=1
        else:
            i+=1
    return sum

if __name__ == '__main__':
    print(f(3124,True))
    print(f(3124,False))
    print(f(20576,False))
    print(f(20576,True))
    print(f(13115,True))