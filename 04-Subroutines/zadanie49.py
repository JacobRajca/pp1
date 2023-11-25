def f(dice):
    i=0
    highest = 0
    count = 0
    while i < len(dice)-1:
        if i+1 <= len(dice):
            if dice[i] == dice[i+1]:
                count+=1
                if count > highest:
                    highest = count
                    highest_num = int(dice[i])
            else:
                if count > highest:
                    highest = count
                    highest_num = int(dice[i])
                    count = 0
                else:
                    count = 0
            i+=1
        else:
            break
    return highest_num

print(f('5233165554211'))
print(f('2133'))