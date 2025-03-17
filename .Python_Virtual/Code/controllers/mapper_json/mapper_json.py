class MapperJson:
    def __init__(self, topico:str, porta:str, read:bool, write:bool, value:int):
        self.topico = topico
        self.porta = porta
        self.read = read
        self.write = write
        self.value = value