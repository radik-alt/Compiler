import Utils
from Lex import Lex
from Utils import operations, keywords, increment
from Variable import Variable
from firstLab.LexemAnalyz import LexemAnalyz

lexemeList = []
variableList = []
SIZE_TAB = 3
SIZE_INCREMENT = 2


def lexemeProcess():
    with open("lab.txt", "r") as file:
        for line in file:
            len_line = len(line)
            i = 0
            buffer = ""
            while i < len_line:
                if valid(line[i], operations):
                    buffer += line[i]
                elif buffer != "":
                    if buffer in keywords:
                        type = Utils.getLexType(buffer)
                        addLexeme(Utils.getLexType(buffer), 0, buffer)
                    elif buffer in Utils.delimeter:
                        addLexeme(Utils.getLexType(buffer), 1, buffer)
                    elif not buffer[0].isdigit():
                        addLexeme(Utils.getLexType(buffer), 1, buffer)
                    elif buffer.isdigit():
                        addLexeme(Utils.getLexType(buffer), 2, buffer)
                    else:
                        print(f"Лексический анализатор нашел ошибку!\nОшибка на строке: ${line} \nСимвол: ${buffer}")
                        exit()

                    buffer = ""

                if i <= len(line):
                    if line[i:i + SIZE_INCREMENT] in increment:
                        symbol = line[i:i + SIZE_INCREMENT]
                        addLexeme(Utils.getLexType(symbol), 1, symbol)
                        i += 1
                    elif line[i] in operations:
                        symbol = line[i]
                        addLexeme(Utils.getLexType(symbol), 3, symbol)
                elif line[i] in operations:
                    symbol = line[i]
                    addLexeme(Utils.getLexType(symbol), 3, symbol)
                elif line[i] in Utils.delimeter:
                    lexemeList.append([3, line[i]])

                if i < len(line) - SIZE_TAB:
                    if line[i:i + SIZE_TAB] == "   ":
                        symbol = line[i:i + SIZE_TAB]
                        addLexeme(Utils.getLexType(symbol), 0, "tab")
                        i += 3

                i += 1

    return lexemeList


def valid(symbol, single_operators):
    if symbol not in single_operators and symbol != " " and not isEmpty(symbol):
        return True
    return False


def addLexeme(Type: str, id: int, value: str):
    lexemeList.append(Lex(Type, id, value))


def addVariable(id:int, type:str, name: str):
    variableList.append(Variable(id, type, name))


def isEmpty(buffer):
    return buffer == ' ' or buffer == '\n' or input == '\0' or input == '\r\n'


def printLexeme():
    print("Лексемы:")
    for item in lexemeList:
        print(item)


def printVariable():
    print("Перменные: \n")
    for variable in variableList:
        print(variable)


if __name__ == "__main__":
    lexemeProcess()
    printLexeme()
