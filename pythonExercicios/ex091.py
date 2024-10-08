from time import sleep                  # pausas
from random import randint              # sortear os valores
from operator import itemgetter         # pegar uma parte do dicionário (nesse caso, o valor, e não a chave)

jogadores = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6), 'jogador3': randint(1, 6), 'jogador4': randint(1, 6)}
# jogar o dado de cada jogador

# apresentar os valores sorteados com pausas
print('Valores sorteados: ')
sleep(1)
for k, v in jogadores.items():
    print(f'O {k} tirou {v}')
    sleep(1)

#criar o ranking e apresentar com pausas
print('-=' * 14)
print('== RANKING DOS JOGADORES ==')
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)  # ordenar a partir dos valores presentes no dicionário jogadores e do maior para o menor
sleep(1)
for posicao in range(4):
    print(f'{posicao + 1}° lugar: {ranking[posicao][0]} com {ranking[posicao][1]}')
    sleep(1)