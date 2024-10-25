
print('1 - Para criar um dicionário com informações de uma pessoa, você pode utilizar a seguinte solução:')
pessoa = {'nome': 'Paulo', 'idade': 25, 'cidade': 'São Paulo'}
print(f'{pessoa}\n')

print('2 - Para fazer a atualização de um valor, adicionar um item e remover uma informação, você pode usar o seguinte raciocínio:')
print('# Atualização de Idade')
pessoa['idade'] = 31
print(f'{pessoa}\n')

print('# Adicionando Profissão')
pessoa['profissao'] = 'Engenheiro'
print(f'{pessoa}\n')

print('# Remoção de Elemento')
del pessoa['cidade']
print(f'{pessoa}\n')

print('3 - Uma possível abordagem para criar um dicionário que apresente os números de 1 a 5 e seus respectivos quadrados é a seguinte:')
numeros_quadrados = {x: x**2 for x in range(1, 6)}
print(f'{numeros_quadrados}\n')

print('4 - Para verificar a existência de uma chave no dicionário, você pode utilizar a seguinte estrutura:')
pessoa = {'nome': 'Amanda', 'idade': 19, 'cidade': 'São Luís'}
print(f'{pessoa}\n')

if 'nome' in pessoa:
    print("A chave 'nome' existe no dicionário.\n")
else:
    print("A chave 'nome' não existe no dicionário.\n")

print('5 - Para contar a frequência de cada palavra em uma frase, você pode utilizar o seguinte código:')
frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos dias do anos."
contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)

def main():
    pass

if __name__ == '__main__':
    main()