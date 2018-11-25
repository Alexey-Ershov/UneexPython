class Dots:
    def __init__(self, left_bound, right_bound):
        self.left_bound = float(left_bound)
        self.right_bound = float(right_bound)

    def __get_dots(self, dots_num, start=0, stop=None):
        distance = (self.right_bound-self.left_bound) / (dots_num-1)
        dots = []

        if start is None:
            start = 0

        if stop is None:
            stop = dots_num

        for pos in range(start, stop):
            dots.append(self.left_bound + distance*pos)

        return dots

    def __get_one_dot(self, pos, dots_num):
        distance = (self.right_bound-self.left_bound) / (dots_num-1)
        return self.left_bound + distance*pos

    def __getitem__(self, index_or_slice):
        if isinstance(index_or_slice, int):
            return self.__get_dots(index_or_slice)

        elif index_or_slice.step is None:
            return self.__get_one_dot(index_or_slice.start,
                    index_or_slice.stop)

        else:
            return self.__get_dots(index_or_slice.step,
                                   index_or_slice.start,
                                   index_or_slice.stop)
