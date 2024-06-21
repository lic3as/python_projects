n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2

if media < 5:                           # se média menor que 5, reprovado
    print('Média = {}'.format(media))
    print('REPROVADO')
elif media >= 5 and media < 7:          # senão, se média entre 5 e 7, recuperação
    print('Média = {}'.format(media))
    print('RECUPERAÇÃO')
else:                                   # senão (média maior ou igual a 7), aprovado
    print('Média = {}'.format(media))
    print('APROVADO')
