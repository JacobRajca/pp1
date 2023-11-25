buys = float(input('Bank buys EUR: '))
sells = float(input('Bank sells EUR: '))

spread = float(round(sells - buys, 4))
print(f'Spread: {spread}')