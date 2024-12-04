def somar(a=0, b=0, c=0):       # função com parâmetros opcionais, se não forem escritos, o padrão é 0
    # docstrings: texto q virá no help() da função, deescrição dela
    """
    — > Faz a soma de três valores e mostra o resultado na tela
    :param a: primeiro valor (opcional, valor padrão 0)
    :param b: segundo valor (opcional, valor padrão 0)
    :param c: terceiro valor (opcional, valor padrão 0)
    :return: sem retorno
    Função criada por Alice
    """

    s = a + b + c
    print(f"A soma de {a} + {b} + {c} vale {s}")


def retornaSoma(a=0, b=0, c=0):
    """
    — > Função que soma três valores e retorna o resultado
    :param a: primeiro valor
    :param b: segundo valor
    :param c: terceiro valor
    :return: resultado da soma dos valores
    Criada por Alice.
    """
    s = a + b + c
    return s            # retorno da função


r1 = retornaSoma(7, 5, 2)
r2 = retornaSoma(5, 6)
r3 = retornaSoma(1)
print(f'Meus cáclulos deram {r1}, {r2} e {r3}.')


help(retornaSoma)
help(somar)
somar(2, 3, 4)
somar(10, 2)
somar(7)
somar()
