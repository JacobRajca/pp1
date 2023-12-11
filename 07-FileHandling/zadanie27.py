import re

message = 'To be, or not to be, that is the question'
words = re.findall(r'\b\w+\b', message)
count = 0
for element in words:
    count+=1
print(count)