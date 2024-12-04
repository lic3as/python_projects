from time import sleep
from random import randint


def sortear(lst):
    for c in range(0,5):
        lst.append(randint(1, 10))
    print("Sorteando 5 valores da lista: ", end='')
    sleep(0.5)
    for n in lst:
        print(f"{n}", end=' ')
        sleep(0.5)
    print("PRONTO!")


def somaPar(lst):
    soma = 0
    for n in lst:
        if n % 2 == 0:
            soma += n
    print(f"Somando os valores pares de {lst}, temos {soma}")


lista = list()
sortear(lista)
somaPar(lista)
