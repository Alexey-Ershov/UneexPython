class GoddamnedMinotaur():
    def __init__(self):
        self.__A = eval(input())
        self.__len = len(self.__A)
        self.__cur_cell = 0
        if self.__canEscape():
            print('YES')

        else:
            print('NO')

    def __canEscape(self):
        while True:
            
            # print("DEBUG:", self.__cur_cell)

            if self.__cur_cell == self.__len - 1:
                return True

            if not self.__checkpoints.get(self.__cur_cell) is None:
                if self.__cur_cell > 0:
                    self.__cur_cell -= 1
                    continue

                else:
                    return False
            
            forward_cell = self.__cur_cell + self.__A[self.__cur_cell]
            if forward_cell < self.__len:
                # self.__checkpoints.append([self.__cur_cell,
                #                            forward_cell - 1])
                if self.__cur_cell != forward_cell - 1:
                    self.__checkpoints[self.__cur_cell] = forward_cell - 1

                self.__cur_cell = forward_cell

            elif self.__cur_cell != 0:
                # self.__checkpoints.append([self.__cur_cell, None])
                if self.__checkpoints:
                    saved_cur_cell = self.__cur_cell
                    from_, to = self.__checkpoints.popitem()
                    self.__cur_cell = to
                    if from_ != to - 1:
                        self.__checkpoints[from_] = to - 1

                    self.__checkpoints[saved_cur_cell] = None

                else:
                    return False

            else:
                return False


GoddamnedMinotaur()
