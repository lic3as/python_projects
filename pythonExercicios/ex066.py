num = soma = qtd = 0

while True:                 # loop infinito
    num = int(input("Informe um número [999 para parar]: "))
    if num == 999:          # condição de parada 999
        break
    soma += num         # adiciona a soma
    qtd += 1            # incrementa a quantidade

print(f'Você digitou {qtd} valores e a soma entre eles foi {soma}.')
