def f(binary_number):
    i=0
    sum = 0
    while i < len(binary_number):
        if binary_number[i] == '0' or binary_number[i] == '1':
            sum +=1
        i+=1
    if sum == len(binary_number):
        return True
    else:
        return False
    
if __name__ == '__main__':
    print(f('101101'))
    print(f('1311a10100'))