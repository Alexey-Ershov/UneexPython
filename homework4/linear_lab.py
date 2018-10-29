class GoddamnedMinotaur():
    def __init__(self):
        self.__A = eval(input())
        self.__len = len(self.__A)
        if self.__canEscape(0):
            print('YES')

        else:
            print('NO')

    def __canEscape(self, cur_cell):
        if cur_cell == self.__len - 1:
            return True

        forward_cell = cur_cell + self.__A[cur_cell]
        if (self.__canEscape(forward_cell) 
                if forward_cell < self.__len else False):
            return True

        if cur_cell != 0 and self.__A[cur_cell - 1] != 1:
            return self.__canEscape(cur_cell - 1)

        else:
            return False


GoddamnedMinotaur()
