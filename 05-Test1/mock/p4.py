def f(card_number):
    i=0
    new_string = ''
    while i < len(card_number):
        if i > 1 and i < len(card_number)-4:
            new_string = new_string + "*"
        else:
            new_string = new_string + card_number[i]
        i+=1
    return new_string

if __name__ == '__main__':
    print(f('5290312400019022'))