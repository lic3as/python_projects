nordeste = []                                               # lista nordeste
estado1 = {'uf': 'Ceará', 'sigla': 'CE'}                    # dicionário estado do ceará
estado2 = {'uf': 'Rio Grande do Norte', 'sigla': 'RN'}      # dicionário estado do rn

nordeste.append(estado1)                                    # add ce a nordeste
nordeste.append(estado2)                                    # add rn a nordeste

print(nordeste)                                             # printando a lista de dicionários

# na lista, as posições continuam sendo identificadas por números
# nos 2 dicionários, as posições são identificadas pelas chaves
print(nordeste[0]['sigla'])
