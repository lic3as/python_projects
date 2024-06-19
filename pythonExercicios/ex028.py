from random import randint
from time import sleep                  # dar uma pausinha

computador = randint(0, 5)        # número randômico
print('-=-'*20)                         # imprimir -=- 20 vezes (estilizar)
print('Eu estou pensando em um número entre 0 e 5...')
print('-=-'*20)

usuario = int(input('Qual número você acha que é? '))

print('PROCESSANDO...')
sleep(2)                                # dar a impressão de que o computador passou 2s para processar a resposta

if usuario == computador:               # se o palpite for igual ao escolhido, acertou
    print('Acertou! UAU!')
else:                                   # senão, errou
    print('Errou HAHAHA! Eu tinha pensado em {}'.format(computador))
