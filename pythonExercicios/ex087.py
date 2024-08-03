# criar a matriz
matriz = [[], [], []]                                                       # matriz de 3 dimensões
for linha in range(0, 3):                                                   # repetir pra cada nova linha
    for coluna in range(0, 3):                                              # repetir pra cada noca coluna
        num = int(input(f'Digite um valor para [{linha}][{coluna}]: '))     # mostra linha e coluna atuais
        if coluna == 0:                                                     # se a coluna for 0, adicionar na lista 0 da matriz
            matriz[0].append(num)
        elif coluna == 1:                                                   # se a coluna for 1, adicionar na lista 1 da matriz
            matriz[1].append(num)
        elif coluna == 2:                                                   # se a coluna for 2, adicionar na lista 2 da matriz
            matriz[2].append(num)

print('-=' * 30)
# imprimir a matriz
for l in range(0,3):                                                        # percorrer cada linha
    for c in range(0,3):                                                    # percorrer cada coluna
        print(f'[{matriz[c][l]:^5}]', end='')                                # apresentar de acordo com linha e coluna
    print('')                                                               # pular linha a cada nova linha

print('-=' * 30)
# somar os valores pares da matriz
somaPar = 0                                                                 # armazenar a soma dos valores pares
for l in range(0,3):
    for c in range(0,3):
        if matriz[c][l] % 2 == 0:                                           # se o valor for par, adicionar a somaPar
            somaPar += matriz[c][l]
print(f'A soma dos valores pares é {somaPar}.')

# somar os valores da terceira coluna
somaCol3 = 0                                                                # armazenar a soma da coluna 3
for l in range(0,3):                                                        # percorrer as linhas da coluna 3
    somaCol3 += matriz[2][l]
print(f'A soma dos valores da terceira coluna é {somaCol3}.')

# encontrar o maior valor da segunda linha
maiorLine6 = 0                                                              # armazenar o maior valor da linha 2
for c in range(0,3):                                                        # percorrer as colunas da linha 2
    if c == 0:                                                              # se for o primeiro valor, armazenar como maior
        maiorLine6 = matriz[0][1]
    else:
        if matriz[c][1] > maiorLine6:                                       # se o atual for maior que o maior, atualizar
            maiorLine6 = matriz[c][1]
print(f'O maior valor da segunda linha é {maiorLine6}.')
