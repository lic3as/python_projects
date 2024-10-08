# ler um dicionário com nome, sexo e idade
# fazer isso enquanto não quiser parar e ir adicionando os dicionários a uma lista
# no final, mostrar quantas pessoas foram cadastradas, a média da idade, uma lista com as mulheres e uma lista com as pessoas com idade acima da média
# dicionário pra cada pessoa
# lista com os dicionários, lista com as mulheres e lista com as pessoas com idade acima da média

pessoa = dict()
grupo = list()
qtdPessoas = 0
mediaIdade = 0
mulheres = list()
acimaMedia = list()
qtdMulheres = 0
qtdAcima = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if pessoa['sexo'] in 'FM':
            break
        else:
            print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    qtdPessoas += 1                                             # incrementar a quantidade
    mediaIdade += pessoa['idade']                               # somar idade pra calcular a média depois
    if pessoa['sexo'] == 'F':                                   # se for mulher, adicionar a lista de mulheres
        mulheres.append(pessoa.copy())
        qtdMulheres += 1
    grupo.append(pessoa.copy())                                 # adicionar a lista geral
    while True:                                                 # fazer a validação
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continuar in 'SN':
            break
        else:
            print('ERRO! Por favor, digite apenas S ou N.')
    if continuar == 'N':                                        # quando não quiser continuar, para
        break


mediaIdade = mediaIdade/qtdPessoas                              # a média é a soma das idade divido pela quantidade de pessoas
print('-=' * 40)
print(f'-- O grupo tem {qtdPessoas} pessoas.')
print(f'-- A média de idade é de {mediaIdade} anos.')
print(f'-- As mulheres cadastradas foram: ', end='')
for c in range(0, qtdMulheres):
    print(mulheres[c]['nome'], end=' ')
print('')
print(f'-- Lista de pessoas que estão acima da média: ')
for c in range(0, qtdPessoas):
    if grupo[c]['idade'] > mediaIdade:
        acimaMedia.append(grupo[c])
        qtdAcima += 1
for c in range(0, qtdAcima):
    for k, v in acimaMedia[c].items():
        print(f'{k} = {v}; ', end='')
    print('')
print('<< ENCERRADO >>')
