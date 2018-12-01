class DivStr(str):
    def __floordiv__(self, other):
        data_len = len(self)
        ret_list = []
        for i in range(other):
            start = i * (data_len//other)
            ret_list.append(self[start:start + data_len//other])

        return ret_list

    def __mod__(self, other):
        data_len = len(self)
        return self[data_len - data_len%other:]
