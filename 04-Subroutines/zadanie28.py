import isbinary

bin_num = input('Enter binary number: ')
check_number = isbinary.f(bin_num)
msg = f'{bin_num} is binary number: {check_number}'
print(msg)