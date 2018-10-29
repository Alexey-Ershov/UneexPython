class GoddamnedMinotaur():
    def __init__(self):
        self.__A = eval(input())
        self.__len = len(self.__A)
        self.__cur_cell = 0
        self.__white_intervals = []
        self.__back_point = None
        if self.__can_escape():
            print('YES')

        else:
            print('NO')

    def __can_escape(self):
        while True:
            forward_cell = self.__cur_cell + self.__A[self.__cur_cell]
            if self.__back_point is None:
                if self.__cur_cell == self.__len - 1:
                    return True
                                
                if forward_cell < self.__len and \
                        forward_cell != self.__cur_cell:
                    if self.__cur_cell != forward_cell - 1:
                        self.__white_intervals.append(
                                [self.__cur_cell + 1, forward_cell - 1])

                    self.__cur_cell = forward_cell

                else:
                    if len(self.__white_intervals):
                        self.__back_point = self.__cur_cell
                        left_bound, self.__cur_cell = \
                                self.__white_intervals.pop()

                    else:
                        return False

            else:
                if forward_cell > self.__back_point and \
                        forward_cell < self.__len:
                    if left_bound != self.__cur_cell:
                        self.__white_intervals.append(
                                [left_bound, self.__cur_cell - 1])

                    if self.__back_point != forward_cell - 1:
                        self.__white_intervals.append(
                                [self.__back_point + 1, forward_cell - 1])

                    self.__back_point = None

                    self.__cur_cell = forward_cell

                else:
                    if left_bound != self.__cur_cell:
                        self.__cur_cell -= 1

                    elif len(self.__white_intervals):
                        left_bound, self.__cur_cell = \
                                self.__white_intervals.pop()

                    else:
                        return False


GoddamnedMinotaur()
