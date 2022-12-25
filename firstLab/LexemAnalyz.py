import Utils
from Lex import Lex
from LexTypes import LexTypes
from Variable import Variable


class LexemAnalyz():
    lexemeList = []
    variableList = []
    SIZE_TAB = 3
    SIZE_INCREMENT = 2

    def lexemeProcess(self):
        with open("../lab.txt", "r") as file:
            for line in file:
                len_line = len(line)
                i = 0
                buffer = ""
                while i < len_line:
                    if self.valid(line[i], Utils.operations):
                        buffer += line[i]
                    elif buffer != "":
                        print(buffer)
                        if buffer in Utils.keywords:
                            self.addLexeme(Utils.getLexType(buffer), 0, buffer)
                        elif buffer in Utils.delimeter:
                            self.addLexeme(Utils.getLexType(buffer), 1, buffer)
                        elif not buffer[0].isdigit():
                            self.addLexeme(Utils.getLexType(buffer), 1, buffer)
                        elif buffer.isdigit():
                            self.addLexeme(Utils.getLexType(buffer), 2, buffer)
                        else:
                            print(
                                f"Лексический анализатор нашел ошибку!\nОшибка на строке: ${line} \nСимвол: ${buffer}")
                            exit()

                        buffer = ""

                    if i < len(line) - 1:
                        if line[i:i + self.SIZE_INCREMENT] in Utils.increment:
                            symbol = line[i:i + self.SIZE_INCREMENT]
                            self.addLexeme(Utils.getLexType(symbol), 1, symbol)
                            i += 1
                        elif line[i] in Utils.operations:
                            symbol = line[i]
                            self.addLexeme(Utils.getLexType(symbol), 3, symbol)
                    elif line[i] in Utils.operations:
                        symbol = line[i]
                        self.addLexeme(Utils.getLexType(symbol), 3, symbol)
                    elif line[i] in Utils.delimeter:
                        self.lexemeList.append([3, line[i]])

                    if i < len(line) - self.SIZE_TAB:
                        if line[i:i + self.SIZE_TAB] == "   ":
                            symbol = line[i:i + self.SIZE_TAB]
                            self.addLexeme(Utils.getLexType(symbol), 0, "tab")
                            # lexemeList.append([0, "tab"])
                            i += 2

                    i += 1

        print(self.lexemeList)
        return self.lexemeList

    def valid(self, symbol, single_operators) -> bool:
        return symbol not in single_operators and symbol != " " and not self.isEmpty(symbol)

    def addLexeme(self, Type:LexTypes, id: int, value: str):
        self.lexemeList.append(Lex(Type, id, value))

    def addVariable(self, id: int, type: str, name: str):
        self.variableList.append(Variable(id, type, name))

    def isEmpty(self, buffer) -> bool:
        return buffer == ' ' or buffer == '\n' or input == '\0' or input == '\r\n'

    def printLexeme(self):
        print("Лексемы:")
        for item in self.lexemeList:
            print(item)

    def printVariable(self):
        print("Перменные: \n")
        for variable in self.variableList:
            print(variable)
