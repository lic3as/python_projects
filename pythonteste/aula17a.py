num = [2, 5, 9, 1]                                          # lista
num[2] = 3                                                  # uma lista pode ser modificada, diferente de uma tupla
num.append(7)                                               # para adicionar ao fim da lista, usamos o append
num.insert(1, 4)                             # na posição 1, inserir o 4
num.sort()                                                  # para ordenar a lista
print(num)
num.sort(reverse=True)                                      # para ordernar de forma reversa
print(f'A lista {num} tem {len(num)} elementos.')           # len mostra o tamanho da lista
num.pop()                                                   # remove o último elemento
num.pop(1)                                                  # remove o elemento na posição 1
if 7 in num:
    num.remove(7)                                           # se tiver um 7, remove a primeira ocorrência do 7
else:
    print('Não achei nenhum 7 na lista.')                   # se não, avisa
print(num)

