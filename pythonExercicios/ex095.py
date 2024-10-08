# incrementar o ex093 com uma lista com vários jogadores
# o usuário adiciona enquanto não quiser parar
# ao fim, mostrar uma tabela com código do jogador (posição na lista), nome, gols e total
# mostrar os dados do jogador referente a código

jogador = dict()                                            # dicionário com informações do jogador
jogadores = list()                                          # lista para adicionar cada jogador
qtdJogadores = 0
while True:
    jogador['nome'] = str(input('Nome do Jogador: '))
    qtdPartidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    totalGols = 0
    partidas = list()  # gols em cada partida do jogador
    for p in range(0, qtdPartidas):
        partidas.append(int(input(f'Quantos gols na partida {p}? ')))
        totalGols += partidas[p]
    jogador['gols'] = partidas
    jogador['total'] = totalGols
    jogadores.append(jogador.copy())                        # adicionar informações de cada jogador a lista
    qtdJogadores += 1
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continuar in 'SN':
            break
        else:
            print('ERRO! Por favor, digite apenas S ou N.')
    if continuar == 'N':
        break
    print('-' * 60)
print('-=' * 30)
while True:
    print('cod ', end='')
    for i in jogador.keys():
        print(f'{i:<15}', end='')
    print()
    print('-' * 60)
    for k, v in enumerate(jogadores):
        print(f'{k:>4} ', end='')
        for d in v.values():
            print(f'{str(d):<15}', end='')
        print()
    print('-' * 60)
    codigo = int(input('Mostrar dados de qual jogador? (999 para sair) '))
    if codigo == 999:
        break
    elif codigo >= qtdJogadores:
        print('ERRO! O código não existe! Tente novamente.')
        continue
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[codigo]['nome']}:')
        print(f'O jogador {jogadores[codigo]["nome"]} jogou {qtdPartidas} partidas.')
        for p in range(0, qtdPartidas):
            print(f'     => Na partida {p}, fez {jogadores[codigo]['gols'][p]} gols.')
        print(f'Foi um total de {jogadores[codigo]['total']} gols.')
print('<< ENCERRADO >>')
