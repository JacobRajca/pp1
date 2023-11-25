product_amount = int(input('Number of products purchased: '))
product_price = float(input('Product price: '))
sum=0
i = 1
while i <= product_amount:
    if i > 2:
        sum+=product_price*0.75
    else:
        sum+=product_price
    i+=1
print(f'Amount to pay: {float(sum)}')