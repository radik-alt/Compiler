
import Lex
from secondLab.AST import UnarnOperationNode
from secondLab.AST.BinOperation import BinOperation
from secondLab.AST.ExpressionNode import ExpressionNode
from secondLab.AST.NumberNode import NumberNode
from secondLab.AST.StatesmentNode import StatementNode
from secondLab.AST.VariableNode import VariableNode


class Parser:
    token_list: Lex = []
    pos: int = 0
    scope: any = {}

    def __init__(self, token_list):
        self.token_list = token_list

    def require(self):
        print()

    def match(self, expected:list) -> Lex:
        pass

    def getToken(self):
        currentToken = self.token_list[self.pos]
        print(self.token_list)

    def parseCode(self) -> ExpressionNode:
        root = StatementNode()
        while self.pos < len(self.token_list):
            codeStringNode = self.parseExpression()
            root.addNode(codeStringNode)

        return root

    def parseExpression(self) -> ExpressionNode:
        temp = ExpressionNode()
        if self.match() is None:
            printNode = self.parsePrint()
            return printNode

        variableNode = self.parseVariableOrNumber()
        assignOperation = self.match()
        if assignOperation is not None:
            rightFormulaNode = self.parseFormula()
            binaryNode = BinOperation(assignOperation, variableNode, rightFormulaNode)
            return binaryNode

        raise Exception("После переменной ожидается оператор переменной на позиции")

    def parseFormula(self):
        leftNode = None
        operator = self.match()
        while operator is not None:
            rightNode = None
            leftNode = BinOperation(operator, leftNode, rightNode)
            operator = self.match()

    def parsePrint(self) -> ExpressionNode:
        operator = self.match()
        if operator is not None:
            return UnarnOperationNode(operator, self.parseFormula())

        raise Exception(f"Ожидается унарный оператор на позиции {self.pos}")

    def parseParentDelimetr(self) -> ExpressionNode:
        # если по тек позиции token у нас = (
        if self.match() is not None:
            node = self.parseFormula()
            self.require()
            return node
        else:
            return self.parseVariableOrNumber()

    def parseVariableOrNumber(self) -> ExpressionNode:
        number = self.match()
        if number is not None:
            return NumberNode(number)

        variable = self.match()
        if variable is not None:
            return VariableNode(variable)

        raise Exception(f"На такой {self.pos} позиции ожидалась перменная или число")

    def valid_type_data(self, value):
        pass

    def startParser(self, node: ExpressionNode):
        pass
