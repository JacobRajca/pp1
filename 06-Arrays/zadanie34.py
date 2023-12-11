this_tuple = (10,20,30,40,50)
second_tuple = ()
x = list(second_tuple)
i = len(this_tuple)-1
while i >= 0:
    x.append(this_tuple[i])
    i = i -1
second_tuple = tuple(x)
print(second_tuple)