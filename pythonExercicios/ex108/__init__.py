import moeda

p = float(input("Digite um preço: R$ "))
print(f"A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}")
print(f"O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}")
print(f"Aumentando 10% de {moeda.moeda(p)}, temos {moeda.moeda(moeda.aumentar(p, 10))}")
print(f"Dimnuindo 13% de {moeda.moeda(p)}, temos {moeda.moeda()}")
