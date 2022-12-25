from Lex import Lex
from secondLab.AST.ExpressionNode import ExpressionNode


class VariableNode(ExpressionNode):
    variable: Lex

    def __init__(self, token: Lex):
        super().__init__()
        self.variable = token
