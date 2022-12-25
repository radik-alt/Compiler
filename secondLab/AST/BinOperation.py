from Lex import Lex
from secondLab.AST.ExpressionNode import ExpressionNode


class BinOperation(ExpressionNode):
    operator: Lex
    leftNode: ExpressionNode
    rightNode: ExpressionNode

    def __init__(self, operator, leftNode, rightNode):
        super().__init__()
        self.operator = operator
        self.leftNode = leftNode
        self.rightNode = rightNode
