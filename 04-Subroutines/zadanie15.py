def phone_keyboard():
    i=1
    while i<=9:
        if i%3==0:
            print(f'{i-2} {i-1} {i}')
        i+=1

phone_keyboard()