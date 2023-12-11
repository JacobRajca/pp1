arr = [12, 6, 4, 9, 10]

def star(n):
    print(n)
    for element in n:
        print(element)
        i = 0
        new_string = ''
        while i < element:
            new_string+='*'
            i+=1
        return new_string

print(star(arr))