f = open("shopping.txt",'r')
for line in f:
     print(line, end="")
f.close()

with open('shopping.txt','r') as file:
    for line in file:
        print(line, end='')