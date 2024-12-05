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


def resumo (preco, aumento, reducao):
    print("-" * 30)
    print("RESUMO DO VALOR".center(30))
    print("-" * 30)
    print(f"Preço analisado: \t{moeda(preco)}")
    print(f"Dobro do preço: \t{dobro(preco, True)}")
    print(f"Metado dopreço: \t{metade(preco, True)}")
    print(f"{aumento}% de aumento: \t{aumentar(preco, aumento, True)}")
    print(f"{reducao}% de redução: \t{diminuir(preco, reducao, True)}")
    print("-" * 30)
