lista = list()                                              # lista vazia

for c in range(0,5):                                        # repetir 5 vezes
    num = int(input('Digite um valor: '))                   # informar o valor
    if len(lista) == 0 or num > lista[len(lista) - 1]:      # se for o primeiro valor ou se for maior que o último, adiciona ao final
        lista.append(num)
        print('Adicionado ao final da lista...')
    else:                                                   # senão
        pos = len(lista) - 1                                # posição do último elemento
        while num < lista[pos] and pos >= 0:                # enquanto o valor for menor que o valor naquela posição e não chegar ao início
            pos -= 1                                        # volta uma posição
        lista.insert(pos + 1, num)                          # inserir na posição
        print(f'Adicionado na posição {pos + 1} da lista...')

print('=-' * 30)
print(f'Os valores digitados em ordem foram {lista}')
