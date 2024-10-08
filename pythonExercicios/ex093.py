# ler o nome do jogador e quantas partidas ele jogou e adiconar a um dicionário
# fazer uma lista para armazenar a quantidade de gols feita em cada partida, que será acrescentada ao dicionário
# somar a quantidade de gols e armazenar o total no dicionário
# no dicionário: nome, gols em cada partida (lista) e total de gols

jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do Jogador: '))
qtdPartidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
totalGols = 0
for p in range(0, qtdPartidas):
    partidas.append(int(input(f'Quantos gols na partida {p}? ')))
    totalGols += partidas[p]
jogador['gols'] = partidas
jogador['total'] = totalGols

print('-=' * 40)
print(jogador)
print('-=' * 40)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 40)
print(f'O jogador {jogador["nome"]} jogou {qtdPartidas} partidas.')
for p in range(0, qtdPartidas):
    print(f'     => Na partida {p}, fez {partidas[p]} gols.')
print(f'Foi um total de {totalGols} gols.')
