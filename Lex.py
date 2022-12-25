import Utils
from LexTypes import LexTypes


class Lex:
    lex_types:LexTypes
    lex_id: int
    value: str

    def __init__(self, lex_types:LexTypes, lex_id, value):
        self.lex_types = lex_types
        self.lex_id = lex_id
        self.value = value

    def __str__(self):
        return f"Lexeme type: {self.lex_types.name}; lexeme id: {self.lex_id}; value: {self.value}"