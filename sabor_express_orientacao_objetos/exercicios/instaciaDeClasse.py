#Importa a classe Restaurante
from ..modelos.restaurante import Restaurante

#Cria a instância da classe restaurante
restaurante_praca = Restaurante('Praça', 'Brasileira')

#1 - Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_praca da classe Restaurante.
restaurante_praca.categoria = 'Italiana'

#2 - Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.
nome_do_restaurante = restaurante_praca.nome

#3 - Verifique o valor inicial do atributo ativo para a instância restaurante_praca e exiba uma mensagem informando se o restaurante está ativo ou inativo.
if restaurante_praca.ativo:
    print('O restaurante está tivo.')
else:
    print('O restaurante está inativo.')

#4 - Acesse o valor do atributo de classe categoria diretamente da classe Restaurante.
categoria = restaurante_praca.categoria

#5 - Altere o valor do atributo nome para 'Bistrô'.
restaurante_praca.nome = 'Bistrõ'

#6 - Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast Food'.
restaurante_pizza = Restaurante('Pizza Place', 'Fast Food')

#7 - Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.
if restaurante_pizza.categoria == 'Fast Food':
    print('A categoria é Fast Food.')
else:
    print('A categoria não é Fast Food.')

#8 - Mude o estado da instância restaurante_pizza para ativo.
restaurante_pizza.ativo = True

#9 - Imprima no console o nome e a categoria da instância restaurante_praca.
print(f'Nome: {restaurante_praca.nome}, Categoria: {restaurante_praca.categoria}')