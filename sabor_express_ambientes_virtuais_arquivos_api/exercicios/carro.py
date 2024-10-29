from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas, cor):
        super().__init__(marca, modelo)
        self.portas = portas
        self.cor = cor
    
    def __str__(self):
        status = "ligado" if self._ligado else "desligado"
        return f"{self.marca} | {self.modelo} | Portas: {self.portas} | Cor: {self.cor} | Status: {status}"

    def ligar(self):
         self._ligado = not self._ligado