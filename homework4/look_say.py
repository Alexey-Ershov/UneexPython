def ElemGener():
    cur_elem = '1'
    yield cur_elem

    while True:
        saved_cur_elem = cur_elem
        cur_bit = saved_cur_elem[0]
        count_cur_bit = 1
        cur_elem = ""
        
        for i in saved_cur_elem[1:]:
            if i == cur_bit:
                count_cur_bit += 1

            else:
                cur_elem += str(count_cur_bit) + cur_bit
                cur_bit = i
                count_cur_bit = 1

        cur_elem += str(count_cur_bit) + cur_bit
        yield cur_elem

def LookSay():
    elem_gener = ElemGener()
    cur_elem = next(elem_gener)
    while True:
        for bit in cur_elem:
            yield int(bit)

        cur_elem = next(elem_gener)
