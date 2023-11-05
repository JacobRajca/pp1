a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))
semiPerimeter = float((a+b+c)/2)
triangleArea = float((semiPerimeter*(semiPerimeter-a)*(semiPerimeter-b)*(semiPerimeter-c))**(1/2))
triangleCircumference = a+b+c

print(f"Triangle area: {triangleArea}")
print(f"Triangle circumference: {triangleCircumference}")