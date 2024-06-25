soma = 0                                            # armazenar a soma das idade pra calcular a média
maiorIdadeH = 0                                     # armazenar a idade do homem mais velho
maisVelho = ''                                      # armazenar o nome do homem mais velho
menos20M = 0                                        # amrmazenar quantas mulheres tem menos de 20 anos

for pessoa in range(1, 5):
    print('='*5 + ' {}ª PESSOA '.format(pessoa) + '='*5)
    nome = str(input('Nome: ')).strip()             # já eliminar os espaços no começo e fim
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()       # já eliminar os espaços no começo e fim
    soma += idade                                   # adicionar as idades a soma
    if sexo in 'Mm' and idade > maiorIdadeH:        # se for homem e a idade for maior que a do mais velho
            maiorIdadeH = idade                     # atualizar idade
            maisVelho = nome                        # atualizar nome do mais velho
    elif sexo in 'Ff' and idade < 20:               # se for mulher e a idade for menor que 20
            menos20M += 1                           # incrementa as menores de 20

media = soma / 4                                    # média das idades
print('A média de idade do grupo é de {:.1f} anos.'.format(media))

if maisVelho == '':
    print('Não existem homens no grupo.')
else:
    print('O homem mais velho é {} com {} anos.'.format(maisVelho, maiorIdadeH))

if menos20M > 0:
    print('Existem {} mulheres com menos de 20 anos no grupo.'.format(menos20M))
else:
    print('Não existem mulheres com menos de 20 anos no grupo.'.format(menos20M))
