teste = list()
teste.append('Gustavo')
teste.append(40)

galera = list()
galera.append(teste[:])         # adicionar a lista teste a lista galera
print(galera)

teste[0] = 'Maria'              # mudando gustavo pra maria na lista teste
teste[1] = 19                   # mudando 40 pra 19 na lista teste
galera.append(teste[:])         # adicionando novamente com as atualizações
print(galera)

# se eu não colocar o [:] após o nome da lista, o append fará uma ligação entre as 2, então sempre que uma mudar, a outra também vai mudar
# dessa forma, os dois elementos seriam maria e 19
# colocando o [:], funciona normal (lembrando que tem que colocar em todos os appends):

teste[0] = 'João'
teste[1] = 32
galera.append(teste[:])
print(galera)
