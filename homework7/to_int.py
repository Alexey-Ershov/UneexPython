def argToInt(arg):
    if isinstance(arg, float):
        arg = int(arg)

    return arg


def toint(fun):
    def wrapper(*args):
        args = tuple(map(argToInt, args))
        result = argToInt(fun(*args))
        return result

    return wrapper