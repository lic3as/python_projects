# criação dos boletins da turma
boletim = list()                                # boletim de cada aluno
dados = list()                                  # dados temporários de cada aluno

while True:
    dados.append(str(input('Nome: ')))          # pedir o nome
    dados.append(float(input('Nota 1: ')))      # pedir a nota 1
    dados.append(float(input('Nota 2: ')))      # pedir a nota 2
    dados.append((dados[1] + dados[2])/2)       # fazer a média das notas
    boletim.append(dados[:])                    # adicionar os dados a lista de boletins
    dados.clear()                               # limpar os dados para guardar os próximos
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':                        # parar só quando não quiser mais continuar
        break

# apresentação dos boletins da turma
print('-=' * 18)
print('{0:5} '.format('NÚM.') + '{0:20} '.format('NOME') + '{0:5}'.format('MÉDIA'))
print('-' * 36)
for p in range(0, len(boletim)):                # imprimir nome e média de cada aluno
    print('{0:<5} '.format(p) + '{0:20} '.format(boletim[p][0]) + '{0:5.1f}'.format(boletim[p][3]))
print('-' * 36)

# apresentação das notas por aluno escolhido
while True:
    num = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if num == 999:
        break
    print(f'As notas de {boletim[num][0]} são {boletim[num][1]} e {boletim[num][2]}')
    print('-' * 50)
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')

