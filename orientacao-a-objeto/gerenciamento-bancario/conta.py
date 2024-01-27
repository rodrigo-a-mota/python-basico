class Conta:

    def __init__(self, cliente, saldo, limite):
        self.cliente = cliente
        self.saldo = saldo
        self.limite = limite

    def sacar(self, valor):
        if self.saldo >= valor:
            print('Você acabou de sacar: ' + valor)
            self.saldo -= valor
        else:
            print('Saldo insuficiente')

    def depositar(self, valor):
        if valor >= 1:
            print('Você depositou: ', + valor)
            self.saldo += valor
        else:
            print('O valor depositado não pode ser zero')

    def consultar(self):
        print('seu saldo: ', self.saldo)