class LetterAttr:
    def __getattr__(self, name):
        self.__dict__[name] = name
        return name

    def __setattr__(self, name, value):
        res_value = ""
        for char in value:
            if char in name:
                res_value += char

        self.__dict__[name] = res_value
