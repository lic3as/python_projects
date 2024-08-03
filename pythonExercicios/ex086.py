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
for l in range(0,3):                                                        # percorrer cada linha
    for c in range(0,3):                                                    # percorrer cada coluna
        print(f'[{matriz[c][l]:^5}]', end='')                                # apresentar de acordo com linha e coluna
    print('')                                                               # pular linha a cada nova linha
