def no_3_ones(num):
    if num == 1:
        return 2
    
    elif num == 2:
        return 4
    
    elif num == 3:
        return 7

    else:
        return no_3_ones(num - 1) + no_3_ones(num - 2) + no_3_ones(num - 3)


num = int(input())
print(no_3_ones(num))
