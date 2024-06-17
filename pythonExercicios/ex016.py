from math import trunc  # importando o método para trunar o número (pegar somente a parte antes da vírgula

num = float(input('Digite um número real: '))

print('A parte inteira do número {} é {}'.format(num, trunc(num)))
# também dá pra fazer a mesma coisa com o int() sem utilizar importações
