S = tuple(int(i) for i in input().split(','))


def second_max(S):
    max_item = second_max_item = S[0]
    
    for i in S[1:]:
        if i > max_item:
            if max_item > second_max_item:
                second_max_item = max_item
            max_item = i
        
        elif ((i < max_item) and
                (max_item == second_max_item or i > second_max_item)):
            second_max_item = i

    if max_item == second_max_item:
        return 'NO'
    else:
        return second_max_item


print(second_max(S))
