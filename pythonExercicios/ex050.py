soma = 0
pares = 0

for c in range(1, 7):
    num = int(input('Informe o {}º valor: '.format(c)))         # informa 6 valores
    if num % 2 == 0:                                            # adicionar a soma somente se for par
        soma += num
        pares += 1                                              # incrementa a quantidade de pares
print('Você informou {} números pares e a soma deles é \033[33m{}\033[m.'.format(pares, soma))
