import LexTypes

lexTypes = [
    "ParsingError",
    "DataType",
    "Variable",
    "Delimeter",
    "Identifier",
    "Constant",
    "Operation"
]

keywords = ["for", "range", "in"]
operations = [">", "<", "=", "+", ':', '*', '/', '-']
increment = ["<=", ">=", "!=", "==", "+=", "-=", "*=", "/=", "%="]
delimeter = [":", "(", ")", "   ", ":"]


def getLexType(Type: str):
    if Type in operations or Type in increment:
        return LexTypes.LexTypes.Operation
    elif Type in keywords:
        return LexTypes.LexTypes.Identifier
    elif Type in delimeter:
        return LexTypes.LexTypes.Delimeter
    elif Type.isdigit():
        return LexTypes.LexTypes.Constant
    else:
        return LexTypes.LexTypes.Variable


operators = [
    "assign_operation",
    "sum_operation",
    "subtract_operation",
    "multiply_operation",
    "divide_operation",
    "add_amount_operation",
    "subtract_amount_operation",
    "are_equal_operation",
    "more_operation",
    "less_operation",
    "increment_operation",
    "decrement_operation",
    "modulo_operation"
]


def get_operators(operation):
    if operation == "=":
        return operators[0]
    elif operation == "+=":
        return operators[5]
    elif operation == "+":
        return operation[1]
