# Definição básica de uma função
def soma(numero1, numero2):
    return numero1 + numero2


print(soma('1', '2'))


def tem_sete_itens(objeto):
    if len(objeto) == 7:
        return True
    else:
        return False


if tem_sete_itens('Rodrigo'):
    print('Realmente tem sete letras')
else:
    print('Não tem sete letras')
