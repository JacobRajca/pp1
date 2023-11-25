def f(text):
    i=0
    new_string = ''
    while i <len(text):
        if i == 0:
            new_string = new_string + text[i]
        if i > 0:
            new_string = new_string + '-' + text[i]
        i+=1
    return new_string

print(f('University'))
print(f('UE'))
print(f('x'))
print(f(''))