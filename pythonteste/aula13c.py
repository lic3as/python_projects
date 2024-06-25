soma = 0                                                # armazenar a soma

for num in range(0, 10):                                # repetir 10 vezes
    num = int(input('Digite um valor: '))               # pegar um valor
    soma += num                                         # adicionar a soma
print('O somatório de todos os valores foi {}.'.format(soma))
