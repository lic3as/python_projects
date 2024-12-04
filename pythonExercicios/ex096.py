def area(larg, comp):
    a = larg * comp
    print(f"A área de um terreno {larg} x {comp} é de {a}m².")


print("Controle de Terrenos")
print("-" * 30)
largura = float(input("LARGURA (m): "))
comprimento = float(input("COMPRIMENTO (m): "))

area(largura, comprimento)
