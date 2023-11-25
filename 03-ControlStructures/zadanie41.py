pin = '0815'

i = 0

while i < 3:
    pin_entered = input('Enter the PIN code: ')
    if pin != pin_entered:
        print('Incorrect...')
        i+=1
        if i == 3:
            print('Sorry, your payment card has been blocked.')
    else:
        print('Transaction completed')
        break