def no_3_ones(num):
    result = 0
    first, second, third = 2, 4, 7
    
    if num == 3:
        return third
    
    else:
        for i in range(3, num):
            result = first + second + third
            first, second, third = second, third, result
        
        return result


num = int(input())
print(no_3_ones(num))
