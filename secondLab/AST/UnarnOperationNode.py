from Lex import Lex
from secondLab.AST import ExpressionNode


class UnarOperationNode():
    operator:Lex
    operand:ExpressionNode

    def __init__(self, operator, operand):
        self.operator = operator
        self.operand = operand