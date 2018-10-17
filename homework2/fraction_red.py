numenator, denumenator = eval(input())
integer_part = numenator // denumenator
if integer_part != 0:
    numenator -= integer_part * denumenator


def gcd(a, b):
    if a > b:
        a, b = b, a
    b = b % a
    if b != 0:
        return gcd(b, a)
    else:
        return a

def cancel_fraction(numenator, denumenator):
    gcder = gcd(numenator, denumenator)
    if gcder != 1:
        return cancel_fraction(numenator // gcder,
                               denumenator // gcder)
    else:
        return numenator, denumenator

if numenator != 0:
    numenator, denumenator = cancel_fraction(numenator, denumenator)
    if integer_part != 0:
        print('{} {}/{}'.format(integer_part, numenator, denumenator))
    else:
        print('{}/{}'.format(numenator, denumenator))
else:
    print(integer_part)
