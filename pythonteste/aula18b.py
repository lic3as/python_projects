galera = [['João', 18], ['Manu', 14], ['Ronaldo', 31], ['Lia', 27]]         # 4 listas dentro de uma lista
print(galera)
print(galera[0])                                                            # galera na posição 0 é a lista de joão
print(galera[2][0])                                                         # galera na posição 2 é alista de ronaldo, a lista de ronaldo na posição 0 é ronaldo

for nome in galera:                                                         # printar cada nome, posição 0 de cada lista dentro de galera
    print(nome[0])

for pessoa in galera:                                                       # printar o nome e idade da pessoa (pessoa[0] e pessoa[1]
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade.')
