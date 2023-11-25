def sum(n):
    sum_num = 0
    if n > 0:
        sum_num = n+sum(n-1)
        print(sum_num)
    return sum_num
sum(10)