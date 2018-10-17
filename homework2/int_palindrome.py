num = int(input())


def get_digit(pos):
    return (num % 10**pos) // 10**(pos-1)

def num_len(num):
    num //= 10
    if num == 0:
        return 1
    else:
        return num_len(num) + 1

def is_palindrome(left_pos, right_pos):
    if get_digit(left_pos) == get_digit(right_pos):
        if left_pos - right_pos <= 2:
            return True
        else:
            return is_palindrome(left_pos - 1, right_pos + 1)
    else:
        return False


if is_palindrome(num_len(num), 1):
    print('YES')
else:
    print('NO')
