idade  = int(input('Qual a sua idade:'))
peso   = float(input('Qual a seu peso:'))
altura = float(input('Qual a sua altura:'))

if idade >= 18 and peso >= 60 and altura >= 1.70:
    print('Você está apto para o exercito')
else:
    print('Você não está apto para o exercito')
