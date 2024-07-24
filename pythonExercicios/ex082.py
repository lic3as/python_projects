listaGeral = list()

while True:                                         # adicionar a lista geral enquanto o usuário não digitar não
    listaGeral.append(int(input('Digite um valor: ')))
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

listaPares = list()
listaImpares = list()

for p in range(0, len(listaGeral)):                 # percorrer a lista geral
    if listaGeral[p] % 2 == 0:                      # se for par, adiciona ao final da lista de pares
        listaPares.append(listaGeral[p])
    else:                                           # se for ímparl adiicona ao final da lista de ímpares
        listaImpares.append(listaGeral[p])

print('-=' * 30)
print(f'A lista completa é {listaGeral}')
print(f'A lista de pares é {listaPares}')
print(f'A lista de ímpares é {listaImpares}')
