import re

message = 'To be, or not to be, that is the question'

vowels = re.findall('[aeiouAeiou]',message)
count = 0
for element in vowels:
    count+=1
print(count)