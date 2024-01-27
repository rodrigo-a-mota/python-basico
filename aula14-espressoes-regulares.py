import re

string_de_teste = 'o gato é bonito'

ex = re.search(r'gato', string_de_teste)

# /w+, ex{3, 4}, ex{3}

if ex:
    print(ex.group())
else:
    print('Padrão não encontrado!')
