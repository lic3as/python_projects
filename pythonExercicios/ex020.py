from random import shuffle

aluno1 = str(input('Digite o nome do primeiro aluno: '))
aluno2 = str(input('Digite o nome do segundo aluno: '))
aluno3 = str(input('Digite o nome do terceiro aluno: '))
aluno4 = str(input('Digite o nome do quarto aluno: '))

ordem = [1, 2, 3, 4]    # sortear (reordenar) os números para cada aluno
shuffle(ordem)

print('Na apresentação,')
print('{} será o {}'.format(aluno1, ordem[0]))
print('{} será o {}'.format(aluno2, ordem[1]))
print('{} será o {}'.format(aluno3, ordem[2]))
print('{} será o {}'.format(aluno4, ordem[3]))