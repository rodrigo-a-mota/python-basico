from veiculo import Veiculo
from carro import Carro

caminhao_rosa = Veiculo('rosa', 6, 'mercedes', 10)

print('Veiculo Rosa')
print(caminhao_rosa.cor)
print(caminhao_rosa.rodas)
print(caminhao_rosa.marca)
print(caminhao_rosa.tanque)

caminhao_rosa.abastecer(30)

print(caminhao_rosa.tanque)

carro_azul = Carro('azul', 'Honda', 20)

print('Veiculo Azul')
print(carro_azul.cor)
print(carro_azul.rodas)
print(carro_azul.marca)
print(carro_azul.tanque)

