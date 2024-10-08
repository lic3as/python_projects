estado = dict()                                         # dicionário de dados do estado
brasil = list()                                         # lista de estados do brasil

for c in range(0, 3):                                   # adicionar 3 novos estados
    estado['uf'] =  str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy())                        # adcionar a cópia do estado atual à lista (o fatiamento não funciona pra dicionário, tem que usar copy)

print(brasil)                                           # imprimir a lista completa
for estado in brasil:                                   # percorrer as posições da lista
    for v in estado.values():                           # percorrer os items do estado
        print(v, end=" ")                               # estado e sigla separados por espaço
    print()                                             # passar pra outra linha