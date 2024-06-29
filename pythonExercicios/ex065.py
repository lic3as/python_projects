media = qtdNum = maior = menor = 0                                          # incializar todas as variáveis com 0
continuar = 'S'                                                             # continuar (S ou N -> N = condição de parada)

while continuar != 'N':                                                     # para quando for N
    num = int(input('Informe um valor: '))
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]   # remover os espaços do início e fim, deixar maiúsculo e pegar só a primeira letra
    media += num                                                            # adicionar a média
    qtdNum += 1                                                             # incrementar a quantidade de números
    if qtdNum == 1:                                                         # se for o primeiro, coloca como maior e menor
        maior = menor = num
    else:                                                                   # senão
        if num > maior:                                                     # se for maior que o maior, atualiza o maior
            maior = num
        elif num < menor:                                                   # se for menor que o menor, atuliza o menor
            menor = num
media /= qtdNum                                                             # dividir a soma dos números pela quantidade deles pra encontrar a média exata
print('Você digitou {} números e a média entre eles foi {:.1f}.'.format(qtdNum, media))
print('O maior valor foi {} e o menor foi {}.'.format(maior, menor))
