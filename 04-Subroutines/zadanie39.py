def f(sentence):
    i=0
    x = len(sentence)
    new_string = ''
    while i < x:
        if sentence[i] == ' ':
            new_string = new_string + ''
        else:
            new_string = new_string + sentence[i]
        i+=1
    return new_string

print(f("integrated development environment"))
print(f("A programming language is a system of notation for writing computer programs"))