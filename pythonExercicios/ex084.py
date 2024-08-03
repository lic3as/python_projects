lista = list()                              # lista guardará todas as listas de dados
dados = list()                              # dados guardará temporariamente o nome e o peso

while True:
    dados.append(str(input('Nome: ')))      # adicionar nome ao fim de dados
    dados.append(float(input('Peso: ')))    # adicionar peso ao fim de dados
    lista.append(dados[:])                  # adicionar uma cópia de dados a lista
    dados.clear()                           # limpar dados para preencher de novo

    continuar = ' '                         # se quer continuar
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

print('-=' * 30)
print(f'Ao todos, você cadastrou {len(lista)} pessoas.')

maior = menor = 0
for pessoa in lista:
    if maior == menor == 0:                 # se for a primeira pessoa, coloca no maior e no menor pra fazer as outras comparações
        maior = pessoa[1]
        menor = pessoa[1]
    else:                                   # senão
        if pessoa[1] > maior:               # se for maior que o maior, atualiza maior
            maior = pessoa[1]
        elif pessoa[1] < menor:             # se for menor que o menor, atualiza menor
            menor = pessoa[1]

print(f'O maior peso foi de {maior:.1f} kg. Peso de ', end='')
for pessoa in lista:
    if pessoa[1] == maior:                  # se forem as pessoas com o maior peso, imprime o nome delas
        print(f'[{pessoa[0]}] ', end='')
print('')

print(f'O menor peso foi de {menor:.1f} kg. Peso de ', end='')
for pessoa in lista:
    if pessoa[1] == menor:                  # se forem as pessoas com o menor peso, imprime o nome delas
        print(f'[{pessoa[0]}]', end='')
