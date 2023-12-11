with open('allproducts.txt','a') as file:
    with open('MeatAndFish.txt','r') as meat:
        for line1 in meat:
            file.write(line1)
    with open('GrainsAndBread.txt','r') as grains:
        for line2 in grains:
            file.write(line2)