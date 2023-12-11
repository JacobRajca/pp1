import re

message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
temperatures = re.findall("\d{2}",message)
# complete the program code
# ...
sum = 0
for element in temperatures:
    sum+=int(element)
print(sum)