# 4) Refatore a classe `ContaBancaria` para utilizar a abordagem "pythonica" na criação de atributos. Utilize propriedades, se necessário.
class ContaBancariaPythonica:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def ativo(self):
        return self._ativo

# 5) Crie uma instância da classe e imprima o valor da propriedade titular.
conta4 = ContaBancariaPythonica("Fernanda", 1500)
print(f"Titular da conta 4: {conta4.titular}")