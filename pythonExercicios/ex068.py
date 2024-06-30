from random import randint
cont = 0                                                                        # contador de vitórias

print('-=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR? ')
print('-=-' * 20)

while True:                                                                     # loop infinito
    valPC = randint(0, 10)                                                # valor aleatório entre 0 e 10
    valJogador = int(input('Diga um valor: '))                                  # valor escolhido pelo jogador
    total = valPC + valJogador                                                  # soma dos valores escolhidos
    jogador = 'a'
    while jogador not in 'PI':                                                  # fazer a validação
        jogador = str(input('Par ou impar? [P/I] ')).strip().upper()[0]         # par ou impar
    if total % 2 == 0:                                                          # se é par ou ímpar
        resultado = 'par'
    else:
        resultado = 'impar'
    print(f'Você jogou {valJogador} e o computador jogou {valPC}.')
    print(f'Total de {total}. \033[33mDeu {resultado}!\033[m')
    print('-' * 60)
    if jogador == resultado.upper()[0]:                                         # se o jogador venceu
        print('\033[32mVOCÊ VENCEU!\033[m')
        print('Vamos jogar novamente...')
        print('-' * 60)
        cont += 1
    else:                                                                       # se perdeu, para
        print('\033[31mGAME OVER!\033[m')
        print(f'Você venceu {cont} vezes.')
        break
