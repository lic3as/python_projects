from datetime import date

maiores = 0             # armazenar os maiores de idade
menores = 0             # armazenar os menores de idade

for c in range (1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    idade = date.today().year - nasc            # calcular a idade da pessoa
    if idade >= 21:                             # se for maior ou igual a 21, aumenta nos maiores
        maiores += 1
    else:                                       # se for menor, aumenta nos menores
        menores += 1

print('{} pessoas já atingiram a maioridade.'.format(maiores))
print('{} pessoas ainda são menores.'.format(menores))