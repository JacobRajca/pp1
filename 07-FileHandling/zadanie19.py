with open('Lorem.txt','r') as file:
    with open('copylines.txt','a') as file2:
        for line in file:
            file2.write(line)