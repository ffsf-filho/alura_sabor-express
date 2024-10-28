from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria, capacidade =0):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self.capacidade = capacidade

        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome.ljust(25)} | {self._categoria.ljust(2)}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome'.ljust(26)}{'Categoria'.ljust(28)}{'Avaliação'.ljust(18)}{'Status'}')

        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(15)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return '✅ Ativo' if self._ativo else '❎ Desativado'
    
    def altera_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)
    
    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 0
        else:
            soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
            quantidade_de_notas = len(self._avaliacao)
            media = round(soma_das_notas/quantidade_de_notas, 1)
            return media