def isNum(str_num):
    if str_num[0] == '-':
        str_num = str_num[1:]

    return str_num.isdecimal()


rpn_stack = []
operations = {'+', '-', '*'}


def doOperation(oper):
    global rpn_stack
    
    second_operand = rpn_stack.pop()
    first_operand = rpn_stack.pop()

    if oper == '+':
        rpn_stack.append(first_operand + second_operand)

    elif oper == '-':
        rpn_stack.append(first_operand - second_operand)

    elif oper == '*':
        rpn_stack.append(first_operand * second_operand)


rpn_input = input().split()
for item in rpn_input:
    if isNum(item):
        rpn_stack.append(int(item))

    elif item in operations:
        doOperation(item)

print(rpn_stack.pop())
