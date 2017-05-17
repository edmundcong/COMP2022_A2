import sys
import structures
import helper

class Node:
    def __init__(self, value, parent=None, children=None):
        self.value = value
        self.parent = parent
        self.children = children

class Tokens:
    def __init__(self, var, rule_id=0, LHS='', RHS='', term_count=0):
        self.variable = var
        self.LHS = LHS
        self.RHS = RHS
        self.term_count = term_count
        self.rule_id = rule_id

class Parser:
    def __init__(self, input_str, eval_flag):  # constructor
        self.input_str = input_str
        self.eval_flag = eval_flag


    def parser_string(self, input_str):
        terminals = structures.terminals
        variables = structures.variables
        parse_table = structures.parse_table
        flag = True

        stack = [Tokens("$"), Tokens("P")]
        expressions = []
        rule_id = 0
        # prev_rule_id = 0
        c = ''
        term_length = 0
        while flag:
                T_obj = stack[len(stack) - 1]  # symbol on top of the stack
                T = T_obj.variable
                # if T is an action token then we
                # construct the tree
                # we do this by taking our the LHS and making that the root
                # and everything on the rHS we make the children
                if (self.eval_flag is False):
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
                        if (self.eval_flag != 'eval'):
                            print "ACCEPTED"
                        else:
                            print 'end of program'
                        flag = False
                elif (T in terminals or T == '$'):
                        if (T == c):
                                prev_obj = stack.pop()
                                # whenever we match a terminal we make a bit of our tree
                                # because a terminal is the smallest bit of our tree
                                expressions.insert(0,Node(T_obj.variable))
                                # check to see if we have an action token sitting on top of the stack
                                temp_T = stack[len(stack) - 1]
                                # if we've encountered a rule
                                # if (temp_T.rule_id != prev_rule_id):
                                #     print 'RULE: ' + temp_T.LHS + ' -> ' + temp_T.RHS
                                #     for var in expressions:
                                #         print 'expression stack value: ' + var.value
                                prev_rule_id = temp_T.rule_id
                                input_str = input_str[term_length:]
                        else:
                                print "REJECTED"
                                break
                elif (T in parse_table and c in parse_table[T] and parse_table[T][c] is not None):
                        # we use a rule here
                        stack.pop() # term = stack.pop()
                        # print T + parse_table[T][c]
                        # stack.append(Node('action_token', T))
                        # push the action token onto stack everytime we pop T above
                        temp = parse_table[T][c]

                        term_pos = 0
                        var_pos = 0
                        temp_stack = []
                        temp = temp.replace(" ", "")  # replace white spaces
                        rule_length = helper.rule_length(temp)
                        while (temp != ''):
                                for terminal in terminals:
                                    term_pos = temp.find(terminal, 0)
                                    if (term_pos == 0):
                                        terminal_length = len(terminal)
                                        # also add action token
                                        temp_stack.append(Tokens(terminal, rule_id, T, parse_table[T][c], terminal_length))
                                        temp = temp[terminal_length:]
                                for variable in variables:
                                    var_pos = temp.find(variable, 0)
                                    if (var_pos == 0):
                                        variable_length = len(variable)
                                        # also add action token
                                        temp_stack.append(Tokens(variable, rule_id, T, parse_table[T][c], variable_length))
                                        temp = temp[variable_length:]

                        temp_stack = temp_stack[::-1]  # reverse elements in temp_stack
                        # append each element in temp_stack to stack
                        map(lambda ele: stack.append(ele), temp_stack)
                else:
                        print "REJECTED"
                        break
                # rule_id += 1
                if not input_str:
                        flag = True

# get first cli arg
if len(sys.argv) > 1:
    input_string = str(sys.argv[1])  # get the first CLI argument

    eval_flag = False
    if (len(sys.argv) == 3): # put edge cases here if they type in ... eval asdas
        eval_flag = str(sys.argv[2])

    with open(input_string, 'r') as grammar_file:
        # read entire file, remove new lines and tabs, and remove trailing white spaces
        curr_line = grammar_file.read().replace('\n', '').replace('\t', "").rstrip()
        test_string = curr_line.replace(" ", "")  # replace white spaces
        test_string = test_string + '$'
        if (not helper.string_valid(test_string)):
            print "ERROR_INVALID_SYMBOL"
        temp = Parser(test_string, eval_flag)
        temp.parser_string(test_string)


