num = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para a conversão: ')
print('[1] para BINÁRIO')
print('[2] para OCTAL')
print('[3] para HEXADECIMAL')
base = int(input('Sua opção: '))

if base == 1:               # se for 1, converte pra binário
    print('O número inteiro {} corresponde ao binário {}'.format(num, bin(num)))        # bin() converte o número pra binário
elif base == 2:             # se for 2, converte pra octal
    print('O número inteiro {} corresponde ao octal {}'.format(num, oct(num)))          # oct() converte o número pra octal
elif base == 3:             # se for 3, converte pra hexadecimal
    print('O número inteiro {} corresponde ao hexadecimal {}'.format(num, hex(num)))    # hex() converte o número pra hexadecimal
else:                       # se apertou algo diferente
    print('Opção inválida.')
