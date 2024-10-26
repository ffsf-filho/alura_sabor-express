import os

def verifica_numero_par_impar():
    numero_inserido = int(input('Digite um número? '))

    if (numero_inserido % 2) == 0:
        print(f'O número {numero_inserido}, digitado é par')
    else:
        print(f'O número {numero_inserido}, digitado é impar')

def classifica_a_sua_idade():
    idade_do_usuario = int(input('Qual é a sua idade? '))

    if 0 <= idade_do_usuario <= 12:
        print('Você é uma criança.')
    elif 13 <= idade_do_usuario <= 18:
        print('Você é um adolecente.')
    elif idade_do_usuario > 18:
        print('Você é um adulto.')
    else:
        print('Idade inválida!')

def verifica_usuario_e_senha():
    nome_usuario = input('Digite o nome do usuário: ')
    senha_usuario = input('Digite a sua senha: ')

    if nome_usuario == 'usuarioTeste' and senha_usuario == '123Teste':
        print('Usuário e senha corretos.')
    else:
        print('Os dados digitados estão incorretos!')

def digite_as_coordenadas():
    coordenada_x = float(input('Digite a coordenada X: '))
    coordenada_y = float(input('Digite a coordenada Y: '))

    if coordenada_x > 0 and coordenada_y > 0:
        print('Primeiro Quadrante.')
    elif coordenada_x < 0 and coordenada_y > 0:
        print('Segundo Quadrante.')
    elif coordenada_x < 0 and coordenada_y < 0:
        print('Terceiro Quadrante.')
    elif coordenada_x > 0 and coordenada_y < 0:
        print('Quarto Quadrante')
    else:
        print('o ponto está localizado no eixo ou origem.')


def menu():
    print('1 - Verifica se o número é par/impar')
    print('2 - Classifica a idade')
    print('3 - Digite usuaário/senha')
    print('4 - Digite as coordenadas (x,y)')
    print('5 - Sair')

    opcao_escolhida = int(input('Escolha uma opção? '))

    match opcao_escolhida:
        case 1:
            verifica_numero_par_impar()
        case 2:
            classifica_a_sua_idade()
        case 3:
            verifica_usuario_e_senha()
        case 4:
            digite_as_coordenadas()
        case 5:
            os.system('cls')
            print('Encerando o sistema ....')
        case _:
            print('A opção escolhida é invalida')

def main():
    menu()

if __name__ == '__main__':
    main()
