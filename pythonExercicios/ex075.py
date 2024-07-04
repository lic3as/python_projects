tupla = (int(input('Digite um número: ')),
         int(input('Digite outro número: ')),
         int(input('Digite mais um número: ')),
         int(input('Digite o último número: ')))

print(f'Você digitou os valores {tupla}')

print(f'O valor 9 apareceu {tupla.count(9)} vezes')             # quantas vezes o 9 apareceu

if 3 in tupla:                                                  # se tiver um 3, encontrar a posição do primeiro 3
    print(f'O valor 3 apareceu na {tupla.index(3) + 1}ª posição')
else:                                                           # se não tiver 3, avisar
    print('O valor 3 não foi digitado em nenhuma posição')

print('Os valores pares digitados foram', end=' ')
for num in tupla:                                               # percorrer a tupla
    if num % 2 == 0:                                            # imprimir somente se for par
        print(num, end=' ')
