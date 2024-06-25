num = int(input('Digite um número inteiro: '))

print('\033[31mTABUADA DA ADIÇÃO DE {}\033[m'.format(num))
print('| ', end='')
for c in range(1, 11):
    print('{} + {} = {} | '.format(num, c, num + c), end='')
print('')

print('\033[32mTABUADA DA SUBTRAÇÃO DE {}\033[m'.format(num))
print('| ', end='')
for c in range(1, 11):
    print('{} - {} = {} | '.format(num, c, num - c), end='')
print('')

print('\033[33mTABUADA DA MULTIPLICAÇÃO DE {}\033[m'.format(num))
print('| ', end='')
for c in range(1, 11):
    print('{} * {} = {} | '.format(num, c, num * c), end='')
print('')

print('\033[34mTABUADA DA DIVISÃO DE {}\033[m'.format(num))
print('| ', end='')
for c in range(1, 11):
    print('{} / {} = {:.1f} | '.format(num, c, num / c), end='')
print('')
