import structures


def print_format(stack_arg, test_string):
    #  left argument to lambda is the accumulated value
    #  and right is the is the current value from the iterable
    formatted_stack = reduce(lambda ele, n_ele: n_ele + ele, stack_arg)
    print test_string + '   ' + formatted_stack


# check if string is composed of terminals in our language
def string_valid(input_string):
    temp_str = input_string
    finished = False
    while (not finished):
        valid_token = False
        for terminal in structures.terminals:
            str_pos = temp_str.find(terminal, 0)
            if (str_pos == 0):
                temp_str = temp_str[len(terminal):]  # eat up string
                valid_token = True
        if (not valid_token):
            return False
        if (temp_str == ''):
            finished = True
    return True
