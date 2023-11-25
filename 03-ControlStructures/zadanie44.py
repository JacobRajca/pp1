number = int(input('Enter number: '))
sum = number
i=0

if number != 0:
    while number != 0:
        number = int(input('Enter number: '))
        i+=1
        sum+=number
    print(f'RESULT: Quantity={i}, Sum={sum}, Mean={sum/i}')