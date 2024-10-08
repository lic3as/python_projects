galera = list()                                     # galera guardará cada lista de dados
maiores = menores = 0                               # guardar a quantidade de maiores e menores

dados = list()                                      # dados guardará temporariamente os dados pra mandar pra galera
for c in range(0, 3):                               # repetir 3 vezes
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])                         # adicionar a cópia de dados ao final de galera
    dados.clear()                                   # limpar dados, é importante adicionar a cópia pra não seja adicionado dados vazio

print(galera)

for p in galera:                                    # percorrer galera
    if p[1] >= 18:                                  # se a idade (p[1]) for maior que 18
        print(f'{p[0]} é maior de idade.')          # imprime o nome (p[0]) e informa que é maior
        maiores += 1                                # incrementa maiores
    else:
        print(f'{p[0]} é menor de idade.')          # imprime o nome (p[1]) e informa que é menor
        menores += 1                                # incrementa menores
        
print(f'Temos {maiores} maiores e {menores} menores de idade na galera.')
