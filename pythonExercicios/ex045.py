from random import randint
from time import sleep

opcoes = ('PEDRA', 'PAPEL', 'TESOURA')                  # lista com as opções

computador = randint(0, 2)                        # jogada do computador

# início:
print('-=-'*20)
print('PEDRA, PAPEL, TESOURA...')
print('-=-'*20)
sleep(1)
print('Vamos ver quem vence? Faça sua jogada!')
sleep(1)
print('''[0] PEDRA
[1] PAPEL
[2] TESOURA''')

jogador = int(input('Digite a sua opção: '))            # jogada do jogador

if computador == 0:                                     # C = pedra
    if jogador == 0:                                    # J = pedra -> empate
        print('-=-' * 20)
        sleep(1)
        print('Você escolheu {}. Eu escolhi {}.'.format(opcoes[jogador], opcoes[computador]))
        sleep(1)
        print('Empate!')
        print('-=-' * 20)
    elif jogador == 1:                                  # J = papel -> J vence
        print('-=-' * 20)
        sleep(1)
        print('Você escolheu {}. Eu escolhi {}.'.format(opcoes[jogador], opcoes[computador]))
        print('Papel embrulha pedra.')
        sleep(1)
        print('Você venceu!')
        print('-=-' * 20)
    elif jogador == 2:                                  # J = tesoura -> C vence
        print('-=-' * 20)
        sleep(1)
        print('Você escolheu {}. Eu escolhi {}.'.format(opcoes[jogador], opcoes[computador]))
        print('Pedra quebra tesoura.')
        sleep(1)
        print('Eu venci!')
        print('-=-' * 20)
    else:  # digitou algo diferente: erro
        print('\033[31mJogada inválida.\033[m')
elif computador == 1:                                   # C = papel
    if jogador == 0:                                    # J = pedra -> C vence
        print('-=-' * 20)
        sleep(1)
        print('Você escolheu {}. Eu escolhi {}.'.format(opcoes[jogador], opcoes[computador]))
        print('Papel embrulha pedra.')
        sleep(1)
        print('Eu venci!')
        print('-=-' * 20)
    elif jogador == 1:                                  # J = papel -> empate
        print('-=-' * 20)
        sleep(1)
        print('Você escolheu {}. Eu escolhi {}.'.format(opcoes[jogador], opcoes[computador]))
        sleep(1)
        print('Empate!')
        print('-=-' * 20)
    elif jogador == 2:                                  # J = tesoura -> J vence
        print('-=-' * 20)
        sleep(1)
        print('Você escolheu {}. Eu escolhi {}.'.format(opcoes[jogador], opcoes[computador]))
        print('Tesoura corta papel.')
        sleep(1)
        print('Você venceu!')
        print('-=-' * 20)
    else:  # digitou algo diferente: erro
        print('\033[31mJogada inválida.\033[m')
elif computador == 2:                                   # C = tesoura
    if jogador == 0:                                    # J = pedra -> J vence
        print('-=-' * 20)
        sleep(1)
        print('Você escolheu {}. Eu escolhi {}.'.format(opcoes[jogador], opcoes[computador]))
        print('Pedra quebra tesoura.')
        sleep(1)
        print('Você venceu!')
        print('-=-' * 20)
    elif jogador == 1:                                  # J = papel -> C vence
        print('-=-' * 20)
        sleep(1)
        print('Você escolheu {}. Eu escolhi {}.'.format(opcoes[jogador], opcoes[computador]))
        print('Tesoura corta papel.')
        sleep(1)
        print('Eu venci!')
        print('-=-' * 20)
    elif jogador == 2:                                  # J = tesoura -> empate
        print('-=-' * 20)
        sleep(1)
        print('Você escolheu {}. Eu escolhi {}.'.format(opcoes[jogador], opcoes[computador]))
        sleep(1)
        print('Empate!')
        print('-=-' * 20)
    else:  # digitou algo diferente: erro
        print('\033[31mJogada inválida.\033[m')
