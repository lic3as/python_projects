from utilidadesCeV import moeda, dado

p = dado.leiaDinheiro("Digite o preço: R$ ")
a = int(input("Informe a porcentagem de aumento: "))
r = int(input("Informe a porcentagem de redução: "))

moeda.resumo(p, a, r)
