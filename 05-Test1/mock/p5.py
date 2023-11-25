def f(binary_number):
    i=0
    x=0
    while i < len(binary_number):
        print(binary_number[i])
        if binary_number[i] == '0' or binary_number[i] == '1':
            x=x
        else:
            x+=1
        i+=1
    if x != 0:
        return False
    else:
        return True

if __name__ == '__main__':
    print(f('101101'))
    print(f('1311a10100'))