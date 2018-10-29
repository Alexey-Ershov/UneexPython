def spiralDigits(M, N):
    spiral_matrix = [['x' for i in range(M)] for j in range(N)]
    cur_digit = 0
    i, j = 0, 0
    cur_direction = 'R'
    for count in range(N * M):
        spiral_matrix[i][j] = cur_digit
        cur_digit = (cur_digit + 1) % 10

        if cur_direction == 'R':
            if j == M - 1 or spiral_matrix[i][j + 1] != 'x':
                cur_direction = 'D'
                i += 1
                
            else:
                j += 1

        elif cur_direction == 'D':
            if i == N - 1 or spiral_matrix[i + 1][j] != 'x':
                cur_direction = 'L'
                j -= 1

            else:
                i += 1

        elif cur_direction == 'L':
            if j == 0 or spiral_matrix[i][j - 1] != 'x':
                cur_direction = 'U'
                i -= 1

            else:
                j -= 1

        elif cur_direction == 'U':
            if i == 0 or spiral_matrix[i - 1][j] != 'x':
                cur_direction = 'R'
                j += 1

            else:
                i -= 1

    return spiral_matrix

def printMatrix(matrix, N, M):
    for i in range(N):
        for j in range(M):
            print("{} ".format(matrix[i][j]), end='')

        print(sep='')


M, N = tuple(int(i) for i in input().split(','))
spiral_matrix = spiralDigits(M, N)
printMatrix(spiral_matrix, N, M)
