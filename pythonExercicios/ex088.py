from time import sleep
from random import randint

print('-' * 40)
print('{:^40}'.format('JOGO NA MEGA SENA'))
print('-' * 40)

qtdJogos = int(input('Quantos jogos você quer que eu sorteie? '))       # qtd de jogos a serem sorteados
print('{:-^40}'.format(f' SORTEANDO {qtdJogos} JOGOS '))

numJogo = list()                                                        # lista com os números do jogo
for jogo in range(0, qtdJogos):                                         # repetir pra qtd de jogos
    for num in range(0, 6):                                             # pegar 6 números aleatórios entre 0 e 60 pra formar um jogo
        numJogo.append(randint(1, 60))
    sleep(1)                                                            # pausinha pra printar o jogo
    print(f'Jogo {jogo + 1}: {numJogo}')
    numJogo.clear()                                                     # limpar pra criar outro jogo
print('{:-^40}'.format(' < BOA SORTE! > '))
