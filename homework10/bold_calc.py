variables = {}

input_str = input()
while input_str:
    if input_str[0] != '#':
        try:
            if '=' in input_str:
                eq_pos = input_str.find('=')
                if not input_str[:eq_pos].isidentifier():
                    raise Exception("invalid identifier" + " '" +
                                    input_str[:eq_pos] + "'")

                if input_str[eq_pos + 1] == '=':
                    raise Exception("invalid assignment" + " '" +
                                    input_str + "'")
                
                variables[input_str[:eq_pos]] = eval(input_str[eq_pos + 1:],
                                                     variables);
            
            else:
                print(eval(input_str, variables))

        except Exception as excp:
            print(excp)

    input_str = input()