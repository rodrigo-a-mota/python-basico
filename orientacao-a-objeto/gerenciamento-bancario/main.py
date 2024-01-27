from cliente import Cliente
from conta import Conta

cliente1 = Cliente('Rodrigo', '608.622.813-26', 27)
conta1   = Conta(cliente1, 0, 1000)

print('Cliente: ', conta1.cliente.nome)
conta1.consultar()
conta1.depositar(10)

print('Cliente: ', conta1.cliente.nome)
conta1.consultar()


