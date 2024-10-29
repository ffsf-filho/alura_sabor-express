from item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    def __init__(self, nome: str, preco: float, descricao: str, tipo : str, tamanho: str):
        super().__init__(nome, preco)
        self.tipo = tipo
        self.tamanho = tamanho
        self.descricao = descricao
    
    def __str__(self):
        return self._nome
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.15)