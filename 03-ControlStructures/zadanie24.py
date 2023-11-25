current_price = 140.00
previous_price = 200.00
price_reduced = 100 - (current_price/previous_price*100)
if price_reduced >= 10:
    print(f'Current product price: {current_price}')
    print(f'Previous product price: {previous_price}')
    print('Buy the product!!')
    print(f'Product price reduced by {int(price_reduced)}%')