def f(palandrome):
    i=0
    x = len(palandrome)
    new_string = ''
    while i < x:
        new_string = palandrome[i] + new_string
        i+=1
    if new_string == palandrome:
        return True
    else:
        return False

print(f("radar"))
print(f("12-11-21"))
print(f("book"))