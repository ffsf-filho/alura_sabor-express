from carro import Carro
from moto import Moto

def main():
    carro1 = Carro("Toyota", "Corolla", 4, 'Preto')
    carro1.ligar()
    carro2 = Carro("Honda", "Civic", 2, 'Prata')
    carro2.ligar()
    carro3 = Carro("Ford", "Fusion", 4, 'Vermelho')

    moto1 = Moto("Harley-Davidson", "Street 750", "Esportiva")
    moto2 = Moto("Honda", "CB 500", "Casual")
    moto2.ligar()
    moto3 = Moto("Yamaha", "MT-09", "Esportiva")

    print(carro1)
    print(carro2)
    print(carro3)

    print(moto1)
    print(moto2)
    print(moto3)

if __name__ == '__main__':
    main()