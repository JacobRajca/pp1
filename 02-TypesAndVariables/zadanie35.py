import math

number = int(input('Enter tree circumference: '))
diameter = number/math.pi

print(f'Tree can be cut down: {diameter>=50}')