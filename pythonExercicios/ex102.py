def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número.
    :param num: número a ser calculado
    :param show: mostra os cálculos do fatorial (opcional)
    :return: sem retorno
    """
    if show:
        f = 1                       # fatorial de 0 é 1
        fatoriais = list()          # guardar as multíplicações
        for c in range(num, 1, -1): # percorrer de num a 1 e ir multiplicando
            f *= c
            fatoriais.append(c)
        fatoriais.append(1)
        print('-' * 40)
        for c in range(0, len(fatoriais) - 1):
            print(f"{fatoriais[c]} x ", end="")
        print(f'1 = {f}' )
    else:
        f = 1  # fatorial de 0 é 1
        for c in range(num, 1, -1):  # percorrer de num a 1 e ir multiplicando
            f *= c
        print('-' * 40)
        print(f"{f}")


fatorial(5, True)
fatorial(5)
