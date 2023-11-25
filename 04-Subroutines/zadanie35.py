def f(number1,number2,operator):
    x = number1
    y = number2
    if operator == '+':
        return x+y
    elif operator == '-':
        return x-y
    elif operator == '*':
        return x*y
    elif operator == '%':
        return x%y
    elif operator == '**':
        return x**y
    else:
        return 'Wrong operator'

print(f(2,3, "+"))
print(f(2,3, "%"))
print(f(2,3, "**"))
print(f(2,3, "*"))
print(f(2,3, "-"))
