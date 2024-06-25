num = int(input('Digite um número inteiro: '))

totDiv = 0                              # armazenar por quantos números foi divisível

for count in range(1, num + 1):         # no intervalo de 1 ao número
    if num % count == 0:                # se for divisível, imprime em azul
        print('\033[34m{}\033[m'.format(count), end=' ')
        totDiv += 1
    else:                               # senão, imprime em vermelho
        print('\033[31m{}\033[m'.format(count), end=' ')

print('')
if totDiv <= 2:                         # um número primo só divisível por 2 números (1 e ele mesmo)
    print('O número \033[32m{} é primo\033[m.'.format(num))
else:                                   # todos os não primos são divisíveis por mais de 2 números
    print('O número \033[32m{} não é primo\033[m e é divisível por {} números.'.format(num, totDiv))
