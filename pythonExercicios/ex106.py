from time import sleep


c = ('\033[m',          # 0 - sem cor
     '\033[0;30;41m',   # 1 - vermelho
     '\033[0;30;42m',   # 2 - verde
     '\033[0;30;43m',   # 3 - amarelo
     '\033[0;30;44m',   # 4 - azul
     '\033[0;30;45m',   # 5 - roxo
     '\033[7;30m'       # 6 - branco
     )


def titulo(msg, cor=0):
    tam = len(msg)
    print(c[cor], end='')
    print('~' * (tam + 4))
    print(f'  {msg}')
    print('~' * (tam + 4))
    print(c[0], end='')


def pyHelp():
    """
    — > Função que imprime as fstrings da função.
    :return: sem retorno.
    """
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    sleep(1)
    funcao = str(input('Função ou biblioteca > '))
    while(funcao.lower() != 'fim'):
        titulo(f'Acessando o manual do comando \'{funcao}\'...', 4)
        sleep(1)
        print(c[5], end='')
        print(help(funcao))
        print(c[0], end='')
        sleep(2)
        titulo('SISTEMA DE AJUDA PyHELP', 2)
        sleep(1)
        funcao = str(input('Função ou biblioteca > '))
    titulo('ATÉ LOGO!', 1)

pyHelp()
