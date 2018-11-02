import re

input_string = input()
reg_expr = input().replace('.', r'\.')
reg_expr = reg_expr.replace('@', '.')

match = re.search(reg_expr, input_string)
if match is None:
    print(-1)

else:
    print(match.start())
