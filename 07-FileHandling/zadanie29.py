import re

with open('grades.txt','r') as file:
    file_content = file.read()

grades = re.findall(r'\d\.\d',file_content)
count = 0
sum = 0
for element in grades:
    sum+= float(element)
    count+=1

print(sum/count)