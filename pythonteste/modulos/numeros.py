from uteis import numeros       # importando pacote do pacote

n = int(input("Digite um valor: "))
fat = numeros.fatorial(n)
print(f"O fatorial de {n} é {fat}.")
print(f"O dobro de {n} é {numeros.dobro(n)}")
