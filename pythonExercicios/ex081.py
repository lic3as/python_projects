listaCres = list()                                      # lista vazia

while True:
    num = int(input('Digite um valor: '))
    listaCres.append(num)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':                                # quando a resposta for não, para
        break

listaCres.sort()                                        # ordenar a lista em ordem crescente
listaDec = list()                                       # lista em ordem decrescente
for p in range(len(listaCres) - 1, -1, -1):             # percorrer a lista crescente ao contrário e adicionar a decrescente
    listaDec.append(listaCres[p])

print('-=' * 30)

print(f'Você digitou {len(listaDec)} elementos.')       # tamanho da lista

print(f'Os valores em ordem decrescente são {listaDec}')

if 5 in listaDec:                                       # checar se tem 5
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
