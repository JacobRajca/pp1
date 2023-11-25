import random

def generate_number():
    num = random.randrange(1,10,1)
    return num

if __name__ == '__main__':
    print(generate_number())