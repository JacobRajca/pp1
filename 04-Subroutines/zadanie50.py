def factorial(n):
    if n==0 or n==1:
        return 1
    
    if n > 1:
        i = n
        while i > 0:
            if i == n:
                sum = n
            else:
                sum = sum * i
            i= i - 1
        return sum

def factorial2(n):
    if n==0 or n == 1:
        return 1
    
    if n > 1:
        return n * factorial2(n-1)

print(factorial(6))
print(factorial2(6))