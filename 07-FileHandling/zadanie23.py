with open('power.txt','a') as file:
    for i in range(1,11):
        file.write(str(i)+','+str(i**2)+','+str(i**3)+','+'\n')