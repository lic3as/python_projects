from time import sleep


def contador(i, f, p):
    print(f"Contagem  de {i} a {f} de {p} em {p}")
    sleep(2)
    if p < 0:
        p *= -1
    elif p == 0:
        p = 1
    if i < f:
        for c in range(i, f + 1, p):
            sleep(0.5)
            print(f'{c} ', end="")
        sleep(0.5)
        print("FIM!")
    else:
        for c in range(i, f - 1, -p):
            sleep(0.5)
            print(f'{c} ', end="")
        sleep(0.5)
        print("FIM!")


def linha():
    print("-=" * 30)


contador(1, 10, 1)
sleep(0.5)
linha()
contador(10, 0, 2)
sleep(0.5)
linha()
print("Agora é a sua vez de personalizar a contagem!")
inicio = int(input("Início: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
sleep(0.5)
linha()
contador(inicio, fim, passo)
