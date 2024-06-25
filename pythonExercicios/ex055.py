maior = menor = 0                                   # incializar as variáveis

for c in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(c)))
    if c == 1:
        maior = menor = peso                        # se for o primeiro laço, não dá pra comparar, armazena o peso no maior e menor
    else:
        if peso > maior:                            # se o peso for maior que o maior, atualizar
            maior = peso
        elif peso < menor:                          # se o peso for menor que o menor, atualizar
            menor = peso

print('O maior peso lido foi de {:.2f}kg e o menor peso lido foi de {:.2f}kg.'.format(maior, menor))
