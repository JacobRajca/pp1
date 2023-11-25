def f(product_code):
    i=0
    while i < len(product_code):
        if i == 0:
            x = int(product_code[i])
        if i == 1:
            y = int(product_code[i])
        if i == 2:
            z = int(product_code[i])
        
        if i == 3:
            sum = x + y + z
            number = sum%7
            if number == int(product_code[i]):
                return True
            else:
                return False
        
        i+=1

print(f('1082'))
print(f('2035'))
print(f('1114'))
print(f('7071'))