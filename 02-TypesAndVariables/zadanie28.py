height = int(input('Enter your height in cm: '))
weight = int(input('Enter your weight in kg: '))

bmi = weight / (height/100)**2

print(f'Your BMI index: {bmi}')
print(f'Correct weight: {bmi>=18.5 and bmi <= 24.9}')