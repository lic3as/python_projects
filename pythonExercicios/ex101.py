def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        v = "NÃO VOTA"
        return idade, v
    elif idade < 18:
        v = "VOTO OPCIONAL"
        return idade, v
    elif idade < 65:
        v = "VOTO OBRIGATÓRIO"
        return idade, v
    else:
        v = "VOTO OPCIONAL"
        return idade, v


print("-" * 30)
anoNasc = int(input("Em que ano você nasceu? "))
vota = voto(anoNasc)
print(f"Com {vota[0]} anos: {vota[1]}")
