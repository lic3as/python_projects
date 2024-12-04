def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input("Digite um número: "))
print(f'O fatorial de {n} é {fatorial(n)}.')


def par(valor):
    if valor % 2 == 0:
        return True
    else:
        return False


num = int(input("Digite outro número: "))
if(par(num)):
    print("O número é par.")
else:
    print("O número é ímpar.")
