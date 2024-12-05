def aumentar(preco, porc, form=False):
    preco += preco * (porc/100)
    if form:
        return moeda(preco)
    else:
        return preco


def diminuir(preco, porc, form=False):
    preco -= preco * (porc / 100)
    if form:
        return moeda(preco)
    else:
        return preco


def dobro(preco, form=False):
    preco *= 2
    if form:
        return moeda(preco)
    else:
        return preco


def metade(preco, form=False):
    preco /= 2
    if form:
        return moeda(preco)
    else:
        return preco


def moeda(preco):
    return f"R$ {preco:.2f}"
