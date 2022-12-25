lexTypes = [
    "ParsingError",
    "DataType",
    "Variable",
    "Delimeter",
    "Identifier",
    "Constant",
    "Operation"
]

keywords = ["for"]
operations = [">", "<", "=", "+", ':', '*', '/', '-']
increment = ["<=", ">=", "!=", "==", "+=", "-=", "*=", "/=", "%="]
delimeter = [":", "(", ")"]


def getLexType(Type: str):
    print(f"{Type} --- Type")
    if Type in operations:
        return lexTypes[6]
    elif Type in keywords:
        return lexTypes[4]
    elif Type in delimeter:
        return lexTypes[3]
    elif Type.isdigit():
        return lexTypes[5]
    else:
        return lexTypes[2]


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
