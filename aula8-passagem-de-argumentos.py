# importando uma biblioteca externa

import sys

argumentos = sys.argv


# print(argumentos)

def soma(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


if argumentos[1] == "soma":
    print(soma(float(argumentos[2]), float(argumentos[3])))
elif argumentos[1] == "sub":
    print(sub(float(argumentos[2]), float(argumentos[3])))
