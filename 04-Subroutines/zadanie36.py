def f(detector):
    i = 0
    sum = 0
    over3 = ''
    while i < len(detector):
        if detector[i] == '+':
            sum+=1
            if sum >= 3:
                over3 = 'X'
        elif detector[i] == '-':
            sum = sum -1
        else:
            sum = sum
        i+=1
    if over3 == 'X':
        return True
    else:
        return False

print(f("+-+++-+---"))
print(f("+-+-+-+-"))
print(f("+-++-+--"))
print(f("+-++-++-+---"))