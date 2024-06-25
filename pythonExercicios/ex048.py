soma = 0                            # armazenar a soma
multitplos = 0                      # armazenar a quantidade de múltiplos

for c in range(1, 501, 2):          # número ímpares entre 1 e 500
    if c % 3 == 0:                  # números múltiplos de 3 entre 1 e 500
        soma += c
        multitplos += 1

print('Entre 1 e 500, existem {} números ímpares que são múltiplos de 3.'.format(multitplos))
print('O somatório de todos esses números é \033[32m{}\033[m.'.format(soma))
