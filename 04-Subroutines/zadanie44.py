def f(password):
    i=0
    new_string = ''
    while i < len(password):
        j=0
        x=0
        while j<len(password):
            if i != j and password[i] == password[j]:
                x+=1
            j+=1
        if x == 0:
            new_string = new_string + password[i]
        i+=1
    if len(new_string) >= 6:
        return True
    else:
        return False

print(f('ax15'))
print(f('book123'))
print(f('a2water3'))
print(f('qwerty'))
print(f(''))