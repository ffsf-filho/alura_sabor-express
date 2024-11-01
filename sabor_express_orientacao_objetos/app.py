from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Gui',10)
restaurante_praca.receber_avaliacao('Lais',8)
restaurante_praca.receber_avaliacao('Emy',5)
restaurante_praca.receber_avaliacao('Maria',7)

restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
restaurante_mexicano.altera_estado()
restaurante_japones = Restaurante('Japa', 'Japonesa')

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()