def f(n):
    i=1
    new_str =''
    while i<=n:
        if i==n:
            new_str = new_str + '*'
        elif i==1 and n==1:
            new_str = new_str + '*'
        else:
            new_str = new_str + '*' + '/'
        i+=1
    return new_str

print(f(4))
print(f(1))