import sys
import structures
import helper

class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children

class Tokens:
    def __init__(self, var, LHS='', RHS='', children_amount=0):
        self.variable = var
        self.LHS = LHS
        self.RHS = RHS
        self.children_amount = children_amount

class Parser:
    def __init__(self, input_str, eval_flag):  # constructor
        self.input_str = input_str
        self.eval_flag = eval_flag

    def tree_print_recursive(self, tree, indent = 0):
        if (tree is None):
            return
        # preorder(node v)
        # {
        # visit(v);
        # for each child w of v
        #     preorder(w);
        # }
        if (indent != 0):
            print (indent * '|') + '||'
        indent += 1
        for ele in tree:
            print (indent * '-') + '>' + ele.value + '<-[DEPTH = ' + str(indent) + ']'
            # print len(ele.children)
            self.tree_print_recursive(ele.children, indent)

    def parser_string(self, input_str):
        terminals = structures.terminals
        variables = structures.variables
        parse_table = structures.parse_table
        flag = True

        stack = [Tokens("$"), Tokens("P")]
        expressions = []
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
                            self.tree_print_recursive(expressions)
                        flag = False
                elif (T == 'action_token'):
                    # check to see if we have an action token sitting on top of the stack
                    curr_action_token = stack.pop()
                    # get number of children
                    number_of_pops = curr_action_token.children_amount
                    # pop a node from the expressions stack to build a new child given the RHS
                    # and then push it bac onto the expressions stack
                    nodes = []
                    # print curr_action_token.LHS + ' -> ' + curr_action_token.RHS + ' #' + str(number_of_pops)
                    # for v in expressions:
                    #     print v.value
                    for i in range(number_of_pops):
                        # nodes.insert(0, expressions.pop())
                        # print expressions[0].value
                        # if
                        # if (curr_action_token.LHS in parse_table and curr_action_token.RHS in parse_table[curr_action_token.LHS] and parse_table[curr_action_token.LHS][curr_action_token.RHS] == expressions[0].value):
                        temp_node = expressions.pop()
                        # print 'v: ' + temp_node.value
                        nodes.append(temp_node)

                    nodes = nodes[::-1]
                    root = Node(curr_action_token.LHS, nodes)
                    # print 'root: ' + root.value
                    # for v in nodes:
                    #     print 'children of this node ^' + v.value
                    expressions.append(root)
                elif (T in terminals or T == '$'):
                        if (T == c):
                                prev_obj = stack.pop()
                                # whenever we match a terminal we make a bit of our tree
                                # because a terminal is the smallest bit of our tree
                                expressions.append(Node(T_obj.variable))
                                # temp_T = stack[len(stack) - 1]
                                # if we've encountered a rule
                                input_str = input_str[term_length:]
                        else:
                                print "REJECTED"
                                break
                elif (T in parse_table and c in parse_table[T] and parse_table[T][c] is not None):
                        # we use a rule here
                        stack.pop() # term = stack.pop()
                        # push the action token onto stack everytime we pop T above
                        temp = parse_table[T][c]
                        term_pos = 0
                        var_pos = 0
                        rule_size = 0
                        temp_stack = []
                        temp = temp.replace(" ", "")  # replace white spaces
                        rule_length = helper.rule_length(temp)
                        while (temp != ''):
                                for terminal in terminals:
                                    term_pos = temp.find(terminal, 0)
                                    if (term_pos == 0):
                                        terminal_length = len(terminal)
                                        rule_size += 1
                                        # also add action token
                                        temp_stack.append(Tokens(terminal))
                                        temp = temp[terminal_length:]
                                for variable in variables:
                                    var_pos = temp.find(variable, 0)
                                    if (var_pos == 0):
                                        variable_length = len(variable)
                                        rule_size += 1
                                        # also add action token
                                        temp_stack.append(Tokens(variable))
                                        temp = temp[variable_length:]
                        stack.append(Tokens('action_token', T, parse_table[T][c], rule_size))
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


