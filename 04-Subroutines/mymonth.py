def month(n):
    months = ['January','February','March','April','May','June','July','August','September','October','November','December']
    return months[n-1]

if __name__ == '__main__':
    print(month(1))
    print(month(3))
    print(month(5))
    print(month(7))