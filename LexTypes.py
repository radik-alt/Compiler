from enum import Enum


class LexTypes(Enum):
    ParsingError = -1,
    DataType = 0,
    Variable = 1,
    Delimeter = 2,
    Identifier = 3,
    Constant = 4,
    Operation = 5