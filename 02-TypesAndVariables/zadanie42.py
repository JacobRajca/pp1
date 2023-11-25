number = input('Enter binary number: ')
if len(number) == 4:
    print(f'Binary number in decimal notation: {8*int(number[0])+4*int(number[1])+2*int(number[2])+1*int(number[3])}')