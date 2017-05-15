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
                        print "ACCEPTED"
                        flag = False
                elif (T in terminals or T == '$'):
                        if (T == c):
                                stack.pop()
                                input_str = input_str[term_length:]
                        else:
                                print "REJECTED"
                                break
                elif (T in parse_table and c in parse_table[T] and parse_table[T][c] is not None):
                        stack.pop()
                        temp = parse_table[T][c]
                        term_pos = 0
                        var_pos = 0
                        temp_stack = []
                        temp = temp.replace(" ", "")  # replace white spaces
                        while (temp != ''):
                                for terminal in terminals:
                                    term_pos = temp.find(terminal, 0)
                                    if (term_pos == 0):
                                        temp_stack.append(terminal)
                                        temp = temp[len(terminal):]
                                for variable in variables:
                                    var_pos = temp.find(variable, 0)
                                    if (var_pos == 0):
                                        temp_stack.append(variable)
                                        temp = temp[len(variable):]
                        temp_stack = temp_stack[::-1]  # reverse elements in temp_stack
                        # append each element in temp_stack to stack
                        map(lambda ele: stack.append(ele), temp_stack)
                else:
                        print "REJECTED"
                        break
                if not input_str:
                        flag = True

# get first cli arg
if len(sys.argv) > 1:
    input_string = str(sys.argv[1])  # get the first CLI argument
    with open(input_string, 'r') as grammar_file:
        # read entire file, remove new lines and tabs, and remove trailing white spaces
        curr_line = grammar_file.read().replace('\n', '').replace('\t', "").rstrip()
        test_string = curr_line.replace(" ", "")  # replace white spaces
        test_string = test_string + '$'
        if (not helper.string_valid(test_string)):
            print "ERROR_INVALID_SYMBOL"
        temp = Parser(test_string)
        temp.parser_string(test_string)
