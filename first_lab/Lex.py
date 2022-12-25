import Utils


class Lex:
    lex_types:str
    lex_id: int
    value: str

    def __init__(self, lex_types, lex_id, value):
        self.lex_types = lex_types
        self.lex_id = lex_id
        self.value = value

    def __str__(self):
        return f"Lexeme type: {self.lex_types}; lexeme id: {self.lex_id}; value: {self.value}"