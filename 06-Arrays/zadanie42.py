import random

def rand_elem(array):
    x = random.randrange(0,len(array))
    return array[x]

print(rand_elem([12,3,143,14,53,2,4,67,7,8,9,11]))