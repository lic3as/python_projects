valores = [[], []]                          # lista contendo 2 litas (pares e ímpares)

for c in range(1, 8):                       # repetir 7 vezes
    num = int(input(f'Digite o {c}° valor: '))
    if num % 2 == 0:                        # se for par colocar na lista 0 de valores
        valores[0].append(num)
    else:                                   # se for ímpar colocar na lista 1 de valores
        valores[1].append(num)

print('-=' * 30)
valores[0].sort()                           # ordenar a lista de pares
print(f'Os valores pares digitados foram {valores[0]}')
valores[1].sort()                           # ordenar a lista de ímpares
print(f'Os valores ímpares digitados foram {valores[1]}')
