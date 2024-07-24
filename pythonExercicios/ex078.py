lista = list()

for n in range(0, 5):                                                       # pegar 5 valores pra lista
    lista.append(int(input(f'Digite um valor para a posição {n}: ')))
print('-=' * 30)

print(f'Você digitou os valores {lista}')                                   # imprimir a lista
print(f'O maior valor digitado foi {max(lista)} nas posições ', end='')     # valor máximo
for c in range(0,5):                                                        # imprimir as posições do valor máximo
    if lista[c] == max(lista):
        print(f'{c}...', end='')

print(f'\nO menor valor digitado foi {min(lista)} nas posições ', end='')    # valor mínimo e posições
for c in range(0,5):                                                         # imprimir as posições do valor mínimo
    if lista[c] == min(lista):
        print(f'{c}...', end='')
