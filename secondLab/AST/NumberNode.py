from Lex import Lex
from secondLab.AST.ExpressionNode import ExpressionNode


class NumberNode(ExpressionNode):

    number:Lex

    def __init__(self, number: Lex):
        super().__init__()
        self.number = number

