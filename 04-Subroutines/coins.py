import math

def f(amount_to_pay):
    sum = 0
    i = 0
    x = amount_to_pay
    while i < x:
        if x/5 >= 1:
            sum = sum + math.floor(x/5)
            x = x - (5*math.floor(x/5))
        elif x/2 >= 1:
            sum = sum + math.floor(x/2)
            x = x- (2*math.floor(x/2))
        else:
            sum = sum + math.floor(x/1)
            x = x-(1*math.floor(x/1))
    return sum

if __name__ == '__main__':
    print(f(23))