lista = list()                          # pode iniciar assim ou com os valores dentro dos colchetes
lista.append(2)
lista.append(7)
lista.append(8)

for v in lista:                         # percorrendo cada elemento
    print(f'{v}...', end='')
print('')

for p, v in enumerate(lista):           # pegando posição e valor com enumerate
    print(f'Na posição {p}, encontrei o valor {v}!')
print('Cheguei ao fim da lista.')

num = list()                            # lista vazia
for cont in range(0,5):                 # repetir 5 vezes para pegar os elementos da lista
    num.append(int(input('Digite um valor: ')))

for n in num:
    print(f'{n}...', end='')

# se fizer uma lista e a e uma lista b
# b = a vai fazer com que elas tenham uma ligação, uma alteração em uma, altera a outra
# para criar uma cópia sem ligação é só fazer: b = a[:]
