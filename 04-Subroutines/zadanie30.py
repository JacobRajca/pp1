import sumdigits

num = int(input('Enter number: '))
even = True
sum_digits = sumdigits.f(num,even)
msg = f'{sum_digits}'
print(msg)