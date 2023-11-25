def f(name):
    new_string =''
    x=0
    i=0
    while i < len(name):
        if i == x:
            new_string = new_string + name[i]
            
        if name[i] == ' ':
            x=i+1
        i+=1
    return new_string

print(f("Internet of Things"))
print(f("For Your Information"))
print(f("Python"))