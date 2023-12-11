import re

with open('Lorem.txt','r') as file:
    file_content = file.read()
    
words = re.findall(r'\b\w{6,}+\b',file_content)
for element in words:
    print(element)