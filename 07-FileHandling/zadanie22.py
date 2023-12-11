import random
with open('randomnumbers.txt','a') as file:
    i=0
    while i < 50:
        num = random.randrange(100,999)
        file.write(str(num)+'\n')
        i+=1
