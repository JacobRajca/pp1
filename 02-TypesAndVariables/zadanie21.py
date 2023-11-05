import math
height = int(input('Insert your height in cm: '))
feet = math.floor(height/30.48)
inch = round((height-feet*30.48)/2.54)
print(f"I am {height}, i.e. {feet} feet and {inch}")