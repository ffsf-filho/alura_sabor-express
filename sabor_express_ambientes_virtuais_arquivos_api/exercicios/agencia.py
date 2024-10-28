from banco import Banco

class Agencia(Banco):
    def __init__(self, nome:str, endereco:str, numero:int):
        super().__init__(nome, endereco)
        self._numero = numero
    
    def __str__(self):
        return f'{self._nome}-{self._numero}'