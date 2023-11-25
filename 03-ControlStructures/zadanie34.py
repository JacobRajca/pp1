money_amount = int(input('Enter the amount in PLN: '))
coin_5 = 0
coin_2 = 0
coin_1 = 0
x = money_amount
i = 1

if x/5 >= 1:
    coin_5=int(x/5)
    x = x - (5*coin_5)
    if x/2 >= 1:
        coin_2 = int(x/2)
        x = x - (2*coin_2)
        if x/1 >= 1:
            coin_1 = int(x/1)
            x = x - (1*coin_1)
        else:
            coin_1=0
    else:
        coin_2 = 0
        if x/1 >= 1:
            coin_1 = int(x/1)
            x = x - (1*coin_1)
        else:
            coin_1=0
else:
    coin_5 = 0
    if x/2 >= 1:
        coin_2 = int(x/2)
        x = x - (2*coin_2)
        if x/1 >= 1:
            coin_1 = int(x/1)
            x = x - (1*coin_1)
        else:
            coin_1=0
    else:
        coin_2 = 0
        if x/1 >= 1:
            coin_1 = int(x/1)
            x = x - (1*coin_1)
        else:
            coin_1=0
                
print(f'The amount of PLN {money_amount} in coins:')
print(f'5 zł - {coin_5}')
print(f'2 zł - {coin_2}')
print(f'1 zł - {coin_1}')