import creditcard

creditcard_number = '5290312400019022'
hashed_number = creditcard.f(creditcard_number)
msg = f'{hashed_number}'
print(msg)