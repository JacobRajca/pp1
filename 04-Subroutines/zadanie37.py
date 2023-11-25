def f(n):
    i = 3
    n1 = 0
    n2 = 1
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n >= 3:
        while i <= n:
            if i >= 3 and n >=3:
                nth = n1 + n2
                n1 = n2
                n2 = nth
            i+=1
        return nth
    else:
        return "Wrong value"


print(f(5))
print(f(9))