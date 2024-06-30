num = 0
while True:                 # loop infinito
    print('-' * 100)
    num = int(input('De qual número você quer ver a tabuada?\n[valor negativo para encerrar] '))
    if num < 0:             # condição de parada = número negativo
        break
    print('-' * 100)
    print('\033[32mTABUADA DA MULTIPLICAÇÃO DE {}\033[m'.format(num))
    for c in range(1, 11):
        print('{} * {} = {}'.format(num, c, num * c))

print('Programa encerrado.')
