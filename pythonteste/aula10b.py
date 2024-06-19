n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2                           # calcular a media das notas
print('A sua média foi {}'.format(media))

if media >= 7:                                  # se a media for maior que 7, o aluno está aprovado
    print('Parabéns, você foi aprovado!')
else:                                           # senão, o aluno está reprovado
    print('Você está reprovado. Estude mais!')
