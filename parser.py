import sys
import structures
import helper

class Parser:
    def __init__(self, input_str):  # constructor
        self.input_str = input_str

    def parser_string(self, input_str):
        terminals = structures.terminals
        variables = structures.variables
        parse_table = structures.parse_table
        flag = True
        stack = ["$", "P"]
        c = ''
        term_length = 0
        while flag:
                T = stack[len(stack) - 1]  # symbol on top of the stack
                # get current symbol
                helper.print_format(stack, input_str)
                for terminal in terminals:
                    str_pos = input_str.find(terminal, 0)
                    if (str_pos == 0):
                        c = terminal
                        term_length = len(terminal)
                if (c not in terminals):
                        print "ERROR_INVALID_SYMBOL"
                        break
                elif (T == c == "$"):
                        print "ACCEPT"
                        flag = False
                elif (T in terminals or T == '$'):
                        if (T == c):
                                stack.pop()
                                input_str = input_str[term_length:]
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
                if not input_str:
                        flag = True

# get first cli arg
input_string = str(sys.argv[1])  # get the first CLI argument
with open(input_string, 'r') as grammar_file:
    for index, line in enumerate(grammar_file):
        curr_line = line.rstrip()
        test_string = curr_line.replace(" ", "")  # replace white spaces
        if (not helper.string_valid(test_string)):
            print "ERROR_INVALID_SYMBOL"
            continue
        temp = Parser(test_string)
        temp.parser_string(test_string)
