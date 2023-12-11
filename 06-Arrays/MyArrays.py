def a(a):
    max_element = max(a)
    i = 0
    second_max = -999
    while i < len(a):
        if a[i] != max_element:
            if second_max < a[i]:
                second_max = a[i]
        i+=1
    return second_max

def b(b):
    max_element = max(b)
    min_element = min(b)
    return max_element - min_element

def c(c):
    for i in range(len(c)):
        for j in range(len(c)-i-1):
            if c[j] > c[j+1]:
                c[j],c[j+1] = c[j+1],c[j]
    return c[len(c)//2]

def d(d):
    max_element = max(d)
    min_element = min(d)
    new_arr = [min_element,max_element]
    return new_arr

def e(e):
    new_string =''
    i=0
    while i < len(e):
        if i == len(e)-1:
            new_string = new_string + str(e[i])
        else:
            new_string = new_string + str(e[i]) + '-'
        i+=1
    return new_string