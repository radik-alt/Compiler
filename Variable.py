class Variable:
    id:int
    type:str
    name: str

    def __init__(self, id, type, name):
      self.id = id
      self.type = type
      self.name = name

    def __str__(self):
        return f"<{self.id}> Variable of type <{self.type}> with name <{self.name}>"