listagem = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9,
            'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99,
            'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.9)
# tupla com a listagem de produto e preço

print('-' * 60)
print('{:^60}'.format('LISTAGEM DE PREÇOS'))
print('-' * 60)

for c in range(0, len(listagem), 2):                            # listagem pulando de 2 em 2
    print('{0:.<50}'.format(listagem[c]), end='')               # produto, que é sempre a posição c
    print('R$ {0:>7.2f}'.format(listagem[c + 1]), end='')       # preço, que é sempre a posição c+1
    print('')

print('-' * 60)
