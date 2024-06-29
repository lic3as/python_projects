n = 1                           # condição de parada (quando for 0, para)
pares = impares = 0             # armazenar pares e ímpares

while n != 0:                   # enquanto for diferente de 0
    n = int(input('Digite um valor: [0 para parar] '))
    if n != 0:                  # se não for 0
        if n % 2 == 0:          # testar se é par e incrementar
            pares += 1
        else:                   # testar se é ímpar e incrementar
            impares += 1

print('Você digitou {} números pares e {} números ímpares.'.format(pares, impares))