n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

if n1 > n2:                                         # se o primeiro valor for maior
    print('O PRIMEIRO valor é maior')
elif n2 > n1:                                       # senão, se o segundo valor for maior
    print('O SEGUNDO valor é maior')
else:                                               # senão, os dois são iguais
    print('Não existe valor maior, os dois são IGUAIS')
