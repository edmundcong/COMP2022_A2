import structures

def rule_length(rule):
  rule_length_counter = 0
  while (rule != ''):
          for terminal in structures.terminals:
              term_pos = rule.find(terminal, 0)
              if (term_pos == 0):
                  terminal_length = len(terminal)
                  rule_length_counter += 1
                  rule = rule[terminal_length:]
          for variable in structures.variables:
              var_pos = rule.find(variable, 0)
              if (var_pos == 0):
                  variable_length = len(variable)
                  rule_length_counter += 1
                  rule = rule[variable_length:]
  return rule_length_counter

def concat_strings(first, second):
    if (type(first) is not str):
      first = first.variable
    if (type(second) is not str):
      second = second.variable
    first = first.replace('action_token', '')
    second = second.replace('action_token', '')
    return first + second

def print_format(stack_arg, test_string):
    #  left argument to lambda is the accumulated value
    #  and right is the is the current value from the iterable
    if (len(stack_arg) > 1):
        formatted_stack = reduce(lambda ele, n_ele: concat_strings(ele, n_ele), stack_arg)
        print test_string + '   ' + formatted_stack
    else:
        last_val = stack_arg[0]
        print test_string + '   ' + last_val.variable


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
        if (temp_str == '' or temp_str == '\n'):
            finished = True
    return True
