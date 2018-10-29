class GoddamnedMinotaur():
    def __init__(self):
        self.__A = eval(input())
        self.__len = len(self.__A)
        self.__cur_cell = 0
        self.__checkpoints = []
        if self.__canEscape():
            print('YES')

        else:
            print('NO')

    def __canEscape(self):
        while True:
            
            # print("DEBUG:", self.__cur_cell)

            if self.__cur_cell == self.__len - 1:
                return True

            if self.__checkpoints.count(self.__cur_cell):
                if self.__cur_cell > 0:
                    self.__cur_cell -= 1
                    continue

                else:
                    return False

            self.__checkpoints.append(self.__cur_cell)
            
            forward_cell = self.__cur_cell + self.__A[self.__cur_cell]
            if forward_cell < self.__len:
                self.__cur_cell = forward_cell

            elif self.__cur_cell != 0:
                self.__cur_cell -= 1

            else:
                return False


GoddamnedMinotaur()
