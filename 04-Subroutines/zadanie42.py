def f(number1,number2,number3):
    if number1 > number2 and number1 > number3 and number2 > number3:
        return number1-number3
    elif number1 > number2 and number1 > number3 and number2 < number3:
        return number1-number2
    elif number1 < number2 and number1 > number3 and number2 > number3:
        return number2-number3
    elif number1 < number2 and number1 < number3 and number2 > number3:
        return number2-number1
    elif number1 > number2 and number1 < number3 and number2 < number3:
        return number3-number2
    elif number1 < number2 and number1 < number3 and number2 < number3:
        return number3-number1
    else:
        return 'Oops'
    
print(f(7,4,9))
print(f(2,12,8))