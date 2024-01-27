# var_verdade = True
# var_falso   = False
#
# if var_verdade == True:
#     print('var_verdade é  verdadeiro')

# == != <> <= >=
# and, or, not

# a = 2
# b = 10
#
# if a > b:
#     print(a, 'é maior que', b)
# else:
#     print(a, 'não é maior que', b)


print('Opções disponível')
print('1 - Hola word')
print('2 - Abacaxi')
print('3 - uva')

option = input('Escolha uma opção: ')

if option == '1':
    print('Você escolheu Hola Word')
elif option == '2':
    print('Você escolheu abacaxi')
elif option == '3':
    print('Você escolheu uva')
else:
    print('Opção escolhida é invalida')
