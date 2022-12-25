from secondLab.AST.ExpressionNode import ExpressionNode


class StatementNode(ExpressionNode):
    codeStrs: list

    def addNode(self, node: ExpressionNode):
        self.codeStrs.append(node)
