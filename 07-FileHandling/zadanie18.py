with open('Lorem.txt','r') as file:
    file_content = file.read()

with open('copy.txt','w') as file:
    file.write(file_content)
