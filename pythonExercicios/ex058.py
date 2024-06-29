from random import randint

computador = randint(0, 10)       # número randômico
print('Oi, sou o seu computador.')
print('Eu estou pensando em um número entre 0 e 10...')

acertou = False                                         # condição de parada
tentativas = 1                                          # armazenar quantidade de tentativas
while not acertou:                                      # enquanto não tiver acertado
    palpite = int(input('Qual o seu palpite? '))        # pedir o palpite
    if palpite == computador:                           # se for igual, acertou
        acertou = True
        if tentativas == 1:                             # se tentativas for 1, parabenizar por acertar de primeira
            print('Parabéns!!! Você acertou de primeira!')
        else:                                           # senão, mostrar as tentativas também
            print('Parabéns! Você conseguiu em {} tentativas.'.format(tentativas))
    else:                                               # se for diferente, errou
        if palpite < computador:                        # se o palpite for menor
            print('Mais. Tente de novo...')
        elif palpite > computador:                      # se o palpite for maior
            print('Menos. Tente de novo...')
        tentativas += 1                                 # incrementa as tentativas
