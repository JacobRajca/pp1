def f(card_number):
    num = ''
    i=0
    while i < len(card_number):
        if i>1 and i<len(card_number)-4:
            num = num + '*'
        else:
            num = num + str(card_number[i])
        i+=1
    return num

if __name__ == '__main__':
    print(f("5290312400019022"))