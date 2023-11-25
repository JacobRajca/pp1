def f(n):
    divide = 0
    i = 1
    while divide < n:
        j=1
        x=0
        while j <= i:
            if i%j==0:
                x+=1
            j+=1
        if x ==2:
            divide+=1
            if divide == n:
                return i
        i+=1
        
print(f(1))
print(f(5))