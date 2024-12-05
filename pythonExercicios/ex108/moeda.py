def aumentar(preco, porc):
    preco += preco * (porc/100)
    return preco


def diminuir(preco, porc):
    preco -= preco * (porc / 100)
    return preco


def dobro(preco):
    preco *= 2
    return preco


def metade(preco):
    preco /= 2
    return preco


def moeda(preco):
    return f"R$ {preco:.2f}"
