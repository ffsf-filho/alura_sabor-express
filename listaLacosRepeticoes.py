import os

lista_de_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_de_nomes = ['Francisco', 'Guilherme', 'Maria', 'Rosa']
lista_de_anos = [1971, 2024]

def percorrer_lista_usando_loop_for():
    for nome in lista_de_nomes:
        print(f'. {nome}\n')
    
def somar_numeros_impares_usando_loop_for():
    soma = 0
    numeros_impares = ''

    for numero in lista_de_numeros:
        if (numero%2) != 0:
            numeros_impares += str(numero) + ' + '
            soma += numero
        
    print(f'A soma dos número {numeros_impares[0:-2]} é igual a {soma}\n')

def imprime_numero_em_ordem_descrescente_usando_loop_for():
    for numero in range(10,0, -1):
        print(f'{numero}\n')

def imprime_a_tabuada_de_um_numero_usando_loop_for():
    try:
        print('Digite um número para obter a tabuada!')
        print('OU "X" para sair')
        valor_digitado = input('Digite um número para obter a tabuada! ')
        print('')

        if valor_digitado.upper() == "X":
            os.system('cls')
            print('Progama encerrado ....')
        else:
            numero = int(valor_digitado)
            for i in range(1, 11, 1):
                print(f'{numero} X {i} = {numero * i}')
    except:
        print('A opção digitada é inválida!')
        input('Digite algo para continuar ')
        imprime_a_tabuada_de_um_numero_usando_loop_for()

def soma_todos_os_numeros_de_uma_lista_usando_loop_for():
    try:
        total = 0
        valores_somados = ''

        for num_list in lista_de_numeros:
            valores_somados += str(num_list) + ' + '
            total += num_list
        
        print(f'A soma do número {valores_somados[0:-2]} é igual a {total}\n')
    except:
        os.system('cls')
        print(f'Ocorreu um problema inesperado ....')

def media_todos_os_numeros_de_uma_lista_usando_loop_for():
    try:
        media = 0
        soma_total = 0
        media_dos_valores = ''

        for num_list in lista_de_numeros:
            media_dos_valores += str(num_list) + ' + '
            soma_total += num_list
        media = soma_total / len(lista_de_numeros)
    
        print(f'A média da soma dos números {media_dos_valores[0:-2]} é igual a {media}\n')
    except Exception as e:
        os.system('cls')
        print(f'Ocorreu um problema inesperado ....\n{e}\n')

def menu():
    os.system('cls')
    print('Escolha uma opção: ')
    print('1 - Percorrer uma lista usando loop for')
    print('2 - Soma números ímpares usando loop for')
    print('3 - Imprimir números em ordem decrescente usando loop for')
    print('4 - Imprimir a tabuada de um números usando loop for')
    print('5 - Imprimir a soma dos números de uma lista usando loop for')
    print('6 - Imprimir a media dos números de uma lista usando loop for')
    print('7 - Sair\n')

    try:
        opcao = int(input('Digite o número da opção escolhida '))

        match opcao:
            case 1:
                percorrer_lista_usando_loop_for()
            case 2:
                somar_numeros_impares_usando_loop_for()
            case 3:
                imprime_numero_em_ordem_descrescente_usando_loop_for()
            case 4:
                imprime_a_tabuada_de_um_numero_usando_loop_for()
            case 5:
                soma_todos_os_numeros_de_uma_lista_usando_loop_for()
            case 6:
                media_todos_os_numeros_de_uma_lista_usando_loop_for()
            case 7:
                os.system('cls')
                print('Programa encerrado ....')
            case _:
                print('A opção digitada é inválida!')
                input('Digite algo para continuar ')
                menu()
    except Exception as e:
        print(f'A opção digitada é inválida! \n{e}\n')
        input('Digite algo para continuar ')
        menu()

def main():
    menu()

if __name__ == '__main__':
    main()