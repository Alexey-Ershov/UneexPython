import math

def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def max_prime(num):
    for i in range(num, 0, -1):
        if is_prime(i):
            return i

N = int(input())
print(max_prime(N))
