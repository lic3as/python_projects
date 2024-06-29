num = int(input('Informe um número para calcular seu fatorial: '))

fatorial = 1                                    # armazenar o valor do fatorial
print('\033[34m{}!\033[m = {} * '.format(num, num), end='')
while num > 1:                                 # enquanto num for maior que 1, fazer as multiplicações
    fatorial *= num                             # multiplicar por fatorial por num
    num -= 1                                    # decrementar num
    if num == 1:                                # quando num for 1, imprimir o =
        print('{} = '.format(num), end='')
    else:
        print('{} * '.format(num), end='')
print('\033[33m{}\033[m'.format(fatorial))      # resultado

# equivalente com for:
'''
num = int(input('Informe um número: '))         # número a calcular o fatorial

fatorial = 1                                    # armazenar o valor do fatorial
print('\033[34m{}!\033[m = '.format(num, num), end='')
for f in range(num, 0, -1):                     # no intervalo de num a 1, decrementando 1
    fatorial *= f                               # multiplicar por fatorial por f
    if f == 1:                                  # quando f for 1, imprimir o =
        print('{} = '.format(f), end='')
    else:
        print('{} * '.format(f), end='')
print('\033[33m{}\033[m'.format(fatorial))      # resultado
'''
