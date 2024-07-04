from random import randint                                  # 5 números aleatórios
tupla = (randint(0, 10), randint(0, 10), randint(0, 10),
         randint(0, 10), randint(0, 10))

print('Os valores sorteados foram: ', end='')               # imprimindo a tupla
for num in tupla:
    print(num, end=' ')

print(f'\nO maior valor sorteado foi {sorted(tupla)[4]}')   # maior valor: faz um sorted e imprime o último
print(f'O menor valor sorteado foi {sorted(tupla)[0]}')     # menor valor: faz um sorted e imprime o primeiro
