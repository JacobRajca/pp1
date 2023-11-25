'''
A text contains any number of words. Define a function f(name) that returns the acronym (first letters of all words). 
'''

def f(name):
    i=0
    new_string = ''
    while i < len(name):
        if i == 0:
            new_string = new_string + name[i]
        else:
            if name[i] == ' ':
                new_string = new_string + name[i+1]
        i+=1
    return new_string

if __name__ == '__main__':
    print(f('Internet of Things'))
    print(f('For Your Information'))
    print(f('Python'))