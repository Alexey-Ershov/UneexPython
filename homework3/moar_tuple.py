def moar(a, b, n):
    mult_b = 0
    for i in b:
        if i % n == 0:
            mult_b += 1

    mult_a = 0
    for i in a:
        if i % n == 0:
            mult_a += 1
            if mult_a > mult_b:
                return True

    return False
