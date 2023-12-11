file_name = input('Enter file name: ')
with open(file_name,'r') as file:
    counter = 0
    for line in file:
        counter+=1
    print(counter)