class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria, capacidade =0, nota_avaliacao =0):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self.capacidade = capacidade
        self.nota_avaliacao = nota_avaliacao

        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome.ljust(25)} | {self._categoria.ljust(2)}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome'.ljust(26)}{'Categoria'.ljust(28)}{'Status'}')

        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return '✅ Ativo' if self._ativo else '❎ Desativado'
    
    def altera_estado(self):
        self._ativo = not self._ativo

    
restaurante_praca = Restaurante('praça', 'Gourmet', 50, 4.5)
restaurante_praca.altera_estado()

restaurante_pizza = Restaurante('pizza express', 'Italiana', 120, 3.8)
restaurantes = [restaurante_praca, restaurante_pizza]

#print(restaurantes)
#print(dir(restaurante_praca),vars(restaurante_praca))
#print(restaurante_pizza)
#print(restaurante_praca)

Restaurante.listar_restaurantes()