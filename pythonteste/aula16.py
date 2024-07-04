lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')           # tupla lanche
# variáveis compostas: tupla (), lista [], dicionário {}
#lanche[1] = 'Coxinha'                                       # tuplas são imutáveis, essa linha dá erro por isso
print(lanche)                                               # mostrar a vaiável completa
print(lanche[2])                                            # mostrar a posição 2 da variável
print(lanche[1:3])                                          # mostrar da posição 1 a 3, ignorando a 3 (1 e 2, apenas)

for comida in lanche:                                       # o for vai mostrar cada elemento da tupla
    print(f'Eu comi {comida}.')

for pos in range(0, len(lanche)):                           # usando for normal para apresentar a posição também
        print(f'Eu comi {lanche[pos]} na posição {pos}.')

for pos, comida in enumerate(lanche):                       # usando o for para tupla com o enumerate para mostrar a posição
    print(f'Eu comi {comida} na posição {pos}.')

print('Eu comi DEMAIS!')

print(sorted(lanche))                                       # sorted ordena a tupla

a = (1, 3, 5, 7)
b = (2, 4, 6)
c = a + b                                                   # o c será a concatenação de a com b
print(c)
# .count() conta quantas vezes determinado elemento apareceu
# .index() mostra em qual índice o elemento está
# del() apaga a tupla da memória
