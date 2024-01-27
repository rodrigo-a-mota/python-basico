# Exemplos de Coleções em python

# Lista (É ordenado)
minha_lista     = ['Rodrigo', 'Mota']

# Tupla (Não é dinâmica)
minha_tupla     = ('Rodrigo', 'Mota')

# Conjunto (Não é ordenando, Busca mais eficiente que tuplas e listas, não tem dados repetidos)
meu_conjunto    = {'Rodrigo', 'Mota', 'Araujo'}

# Dicionario (Não é ordenado, Busca mais eficiente que tuplas e listas)
meu_dicionario  = {'nome': 'Rodrigo', 'idade': 26}

print(minha_tupla[0])

for nome in minha_tupla:
    print(nome)

if 'Rodrigo' in minha_tupla:
    print('Está na coleção')

if 'Rodrigo' in minha_lista:
    print('Está na coleção')

if 'Rodrigo' in meu_conjunto:
    print('Está na coleção')

print(meu_dicionario['idade'])

if 'Rodrigo' in meu_dicionario.values():
    print('Está na coleção')

# iniciando as coleções vazia

lista               = []
tupla               = ()
dicionario          = {}
dicionario_dois     = dict()
conjunto            = set()
