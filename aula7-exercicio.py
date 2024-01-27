def maior_numero(numeros):
    maior = numeros[0]

    for numero in numeros:
        print('\n o numero recebido:', numero, '\n maior', maior, '\n')
        if numero > maior:
            maior = numero
            print('\n maior:', maior, '\n')

    return maior


maior_numero([3, 30, 1, 14.4, 30, 50, 60, 61])


def menor_numero(numeros):
    menor = numeros[0]

    for numero in numeros:
        print('\n o numero recebido:', numero, '\n menor', menor, '\n')
        if numero < menor or menor == 0:
            menor = numero
            print('\n menor:', menor, '\n')

    return menor


menor_numero([37, 30, 58, 14.4, 30, 50, 60, 61])
