test_string = 'print "abc";$'
test_string_t = 'print (1+3);$'
# test_string = test_string_t
# define set for variables and terminals
terminals = {
        "+", "-", "*", "0", "1", "2", "3", "a", "b", "c", "d", "print", "\"", "if", "else", "{", "}", "(", ")", ";", "$"
}
variables = {  # redefine P' to Q and K' to R for key'ing ease
        "P", "Q", "L", "K", "R", "W", "C'", "C", "E", "O", "V", "T"
}
parse_table = {
        "P": {
                "print": "LQ",
                "if": "LQ"
        },
        "Q": {
                "print": "LQ",
                "if": "LQ",
                "}": "",
                "$": ""
        },
        "L": {
                "print": "K;",
                "if": "C'"
        },
        "K": {
                "print": "print R"
        },
        "R": {
                '"': '"W"',
                "(": "E"
        },
        "W": {
                "a": "TW",
                "b": "TW",
                "c": "TW",
                "d": "TW",
                '"': ""
        },
        "C'": {
                "if": "if E { P } C"
        },
        "C": {
                "else": "else { P }",
                "}": "",
                "$": ""
        },
        "E": {
                "0": "V",
                "1": "V",
                "2": "V",
                "3": "V",
                "(": "(EOE)"
        },
        "O": {
                "+": "+",
                "-": "-",
                "*": "*"
        },
        "V": {
                "0": "0",
                "1": "1",
                "2": "2",
                "3": "3"
        },
        "T": {
                "a": "a",
                "b": "b",
                "c": "c",
                "d": "d"
        }
}

test_string = test_string.replace(" ", "") # replace white spaces
flag = True
stack = ["$", "P"]
c = ''
term_length = 0
x = 0
while flag:
        T = stack[len(stack) - 1]  # symbol on top of the stack
        # get current symbol
        print test_string + ' <--> '
        print stack
        for terminal in terminals:
            str_pos = test_string.find(terminal, 0)
            if (str_pos == 0):
                c = terminal
                term_length = len(terminal)
        if (T == c == "$"):
                print "ACCEPT"
                flag = False
        elif (T in terminals or T == '$'):
                if (T == c):
                        stack.pop()
                        test_string = test_string[term_length:]
                else:
                        print "error 1"
                        break
        elif (parse_table[T][c] is not None):
                stack.pop()
                temp = parse_table[T][c]
                term_pos = 0
                var_pos = 0
                temp_stack = []
                temp = temp.replace(" ", "") # replace white spaces
                while (temp != ''):
                        for terminal in terminals:
                            term_pos = temp.find(terminal, 0)
                            if (term_pos == 0):
                                temp_stack.append(terminal)
                                # stack.append(terminal)
                                temp = temp[len(terminal):]
                        for variable in variables:
                            var_pos = temp.find(variable, 0)
                            if (var_pos == 0):
                                temp_stack.append(variable)
                                # stack.append(variable)
                                temp = temp[len(variable):]

                temp_stack = temp_stack[::-1]  # reverse elements in temp_stack
                # append each element in temp_stack to stack
                map(lambda ele: stack.append(ele), temp_stack)
        else:
                print "error 2"
                break
        if not test_string:
                flag = True
