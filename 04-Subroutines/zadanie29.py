import coins

amount_to_pay = int(input('Enter amount to pay: '))
coins_number = coins.f(amount_to_pay)
msg = f'{coins_number}'
print(msg)