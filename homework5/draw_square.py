def squares(w, h, *contents):
    rectangle = [''.join(['.' for i in range(w)]) for j in range(h)]

    for content in contents:
        X, Y, s, c = content
        for line in range(Y, Y + s):
            rectangle[line] = (rectangle[line][:X] +
                               ''.join([c for column in range(X, X + s)]) +
                               rectangle[line][X + s:])

    printRectangle(rectangle)

def printRectangle(rectangle):
    for line in rectangle:
        print(line)
