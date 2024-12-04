from time import sleep


def linha():
    print("-=" * 30)


def maiorValor(* num):
    maior = 0
    for n in num:
       if n > maior:
            maior = n
    print("Analisando os valores passados...")
    for n in num:
        print(f"{n}", end=" ")
        sleep(0.5)
    print(f"foram informados {len(num)} valores ao todo.")
    print(f'O maior número informado foi {maior}.')


linha()
maiorValor(9, 4, 5, 2, 1, 92, 73)
linha()
maiorValor(3, 5, 2, 8, 7)
linha()
maiorValor()
