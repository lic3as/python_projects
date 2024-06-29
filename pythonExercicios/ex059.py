n1 = int(input('Informe o primeiro valor: '))
n2 = int(input('Informe o segundo valor: '))

opcao = 0
while opcao != 5:               # parar quando a opção for 5
    print('.'*40)
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa 
''', end='')
    opcao = int(input('>>> Informe a opção: '))

    if opcao == 1:              # se quer somar os 2 valores
        print('O resultado de {} + {} é {}.'.format(n1, n2, n1 + n2))
    elif opcao == 2:            # se quer multiplicar os 2 valores
        print('O resultado de {} * {} é {}.'.format(n1, n2, n1 * n2))
    elif opcao == 3:            # se quer saber qual o maior dos 2 valores
        if n1 > n2:             # se n1 for maior
            print('{} é maior que {}.'.format(n1, n2))
        elif n1 == n2:          # se forem iguais
            print('Os dois valores são iguais.')
        else:                   # se n2 for maior
            print('{} é maior que {}.'.format(n2, n1))
    elif opcao == 4:            # se quer informar novos valores
        n1 = int(input('Informe o primeiro valor: '))
        n2 = int(input('Informe o segundo valor: '))
    elif opcao != 5:
        print('Opção inválida.')
print('Fim do programa.')
