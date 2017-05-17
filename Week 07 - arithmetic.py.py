"""The evaluate method will return a representation of evaluating the subtree
rooted at this tree node. Subtrees that are arithmetic expressions will
return a number, but note that some of the subtrees aren't arithmetic
expressions (e.g. a subtree might just be a "(" or an operator like "+")

note: currently this code is incomplete, it will not execute successfully.
You will need to implement the sections marked TODO"""


class TerminalNode():
    """This is a terminal symbol"""
    def __init__(self, element):
        self.element = element
    def evaluate(self):
        """This simply evaluates as the contained string (i.e. the terminal)"""
        return self.element
    def __str__(self):
        return self.element

class ValueNode():
    """This corresponds to the rules V -> 0 | 1 | 2"""
    def __init__(self, child):
        self.child = child
    def evaluate(self):
        #ValueNodes link to TerminalNodes, so they simply evaluate as the string
        #contained in that TerminalNode (i.e. the terminal)
        return int(self.child.evaluate())
    def __str__(self):
        return str(self.child)

class OperationNode():
    """This corresponds to the rules O -> + | - | *"""
    def __init__(self, child):
        self.child = child
    def evaluate(self):
        return str(self.child)
    def __str__(self):
        return str(self.child)

class BinaryExpressionNode():
    """This corresponds to the rule E -> (EOE)"""
    def __init__(self, left_bracket, e1, operation, e2, right_bracket):
        self.left_bracket = left_bracket
        self.e1 = e1
        self.operation = operation
        self.e2 = e2
        self.right_bracket = right_bracket
    def evaluate(self):
        #apply the appropriate operation to the two evaluated expressions
        operation = self.operation.evaluate()
        lhs = self.e1.evaluate()
        rhs = self.e2.evaluate()
        print rhs
        if operation == '+':
            return int(lhs) + int(rhs)
        elif operation == '-':
            return int(lhs) - int(rhs)
        elif operation == '*':
            return int(lhs) * int(rhs)
        else:
            return None #it would be better to raise an exception
    def __str__(self):
        return "{}{}{}{}{}".format(str(self.left_bracket), str(self.e1), str(self.operation), str(self.e2), str(self.right_bracket))

class ValueExpressionNode():
    """This corresponds to the rule E -> V"""
    def __init__(self, child):
        self.child = child
    def evaluate(self):
        return str(self.child)
    def __str__(self):
        return str(self.child)



if __name__ == '__main__':

    """Example (1+(3-2))

         E
    / / |  \    \
  /  /  |    \    \
 (  E   O     E    )
    |   |     |
    V   +     E
    |     / / | \ \
    1     ( E O E )
            | | |
            V - V
            |   |
            3   2
"""

    tree = BinaryExpressionNode(
        TerminalNode("("),
        ValueExpressionNode(ValueNode(TerminalNode("1"))),
        OperationNode(TerminalNode("+")),
        BinaryExpressionNode(
            TerminalNode("("),
            ValueExpressionNode(ValueNode(TerminalNode("3"))),
            OperationNode(TerminalNode("-")),
            ValueExpressionNode(ValueNode(TerminalNode("2"))),
            TerminalNode(")")
        ),
        TerminalNode(")")
    )

    print(str(tree)) #this should output "(1+(3-2))"
    print(tree.evaluate()) #this should output "2"
