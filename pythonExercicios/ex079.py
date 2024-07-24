lista = list()                                          # lista vazia

while True:
    num = int(input('Digite um valor: '))               # informa um número
    if num not in lista:                                # se não estiver na lista, adiciona
        print('Valor adicionado com sucesso!')
        lista.append(num)
    else:                                               # se estiver na lista, não adiciona
        print('Valor duplicado! Não vou adicionar.')
    continuar = ' '
    while continuar not in 'SN':                        # fazer a validação
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':                                # se não quiser continuar, sai do loop
        break
print('-=' * 30)
lista.sort()                                            # ordenar a lista
print(f'Você digitou os valores {lista}')               # imprimir no final
