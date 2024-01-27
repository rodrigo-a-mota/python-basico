
quantidade = int(input('Quantas pessoas você quer convidar: '))
pessoas    = []
index      = 0

while index < quantidade:
    pessoas.append(input('Diga o nome do convidado ' + str(index + 1) + ':'))
    index += 1

print('========================================================')
print('================== Usando o while ======================')
print('========================================================')
print(pessoas)
print('========================================================')

pessoas = []

for index in range(quantidade):
    pessoas.append(
        input('Diga o nome do convidado ' + str(index + 1) + ':'))

print('========================================================')
print('================== Usando o for ========================')
print('========================================================')
print(pessoas)
print('========================================================')
