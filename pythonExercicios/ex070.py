total = maisMil = cont = precoBarato = 0
nomeBarato = ''

print('-' * 40)
print('ALICE ATACADISTA')
print('-' * 40)
while True:                                         # loop infinito
    nome = str(input('Nome do produto: ')).strip()
    preco = int(input('Preço: R$ '))
    total += preco                                  # soma preço no total
    cont += 1                                       # contador de produtos, pra saber quando é o primeiro
    if cont == 1 or preco < precoBarato:            # se for o primeiro ou for mais barato que o mais barato
        precoBarato = preco
        nomeBarato = nome
    if preco >= 1000:                               # se custar mais de 1000, incrementa maisMil
        maisMil += 1
    continuar = ' '
    while continuar not in 'SN':                    # fazer a validação
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':                            # condição de parada = N
        break
print('-' * 40)
print(f'O total da compra foi R$ {total:.2f}.')
print(f'Foram comprados {maisMil} produtos custando mais de R$ 1000.')
print(f'O produto mais barato foi {nomeBarato}, custando R$ {precoBarato:.2f}.')
