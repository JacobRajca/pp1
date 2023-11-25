def count_letter_e(x):
    text_len = len(x)
    i = 0
    sum = 0
    while i<text_len:
        if x[i] == 'e':
            sum+=1
        i+=1
    return sum

if __name__ == '__main__':
    print(count_letter_e('You never get a second chance to make a first impression'))