def f(expresion):
    x=expresion
    i=0
    prev_num = 0
    operator = ''
    current_num = 0
    y = 0
    sum = 0
    while i < len(x):
        if i == 0:
            prev_num = int(x[i])
    
        if x[i] == '+' or x[i] == '-':
            operator = x[i]
            y = i + 1
    
        if i == y:
            current_num = int(x[i])
            if operator == '+':
                sum = prev_num + current_num
                prev_num = sum
            elif operator == '-':
                sum = prev_num - current_num
                prev_num = sum
            else:
                sum=sum
        i+=1
    return sum

print(f('2+3-4+5-0'))