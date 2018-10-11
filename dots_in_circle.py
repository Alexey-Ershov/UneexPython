import math

x, y, r = eval(input())
is_every_belong = True


def distance(a, b, x, y):
    return math.sqrt((a-x)**2 + (b-y)**2)

def dots_in_circle():
    a, b = eval(input())
    if a != 0 or b != 0:
        if distance(a, b, x, y) <= r:
            dots_in_circle()
        else:
            global is_every_belong
            is_every_belong = False


dots_in_circle()
if is_every_belong:
    print('YES')
else:
    print('NO')