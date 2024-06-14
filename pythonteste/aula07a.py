# OPERADORES ARITMÉTICOS:
# + adição
# - subtração
# * multiplicação
# / divisão
# ** potência (ou pode ser feita com a função pow(b,e), porém perde a ordem de precedência)
# // divisão inteira
# % resto da divisão

#calcular a reiz quadrada é o mesmo que criar a potência dele com 1/2, ou seja, raiz quadrada de 4 é 4**(1/2)

# ORDEM DE PRECEDÊNCIA:
# 1. ()
# 2. **
# 3. * / // %
# 4. + -

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

s = n1 + n2     # soma
m = n1 * n2     # multiplicação
d = n1 / n2     # divisão
di = n1 // n2   # divisão inteira
e = n1 ** n2    # exponenciação/potência

print('A soma é {}, o produto é {} e a divisão é {}'. format(s, m, d))
print('A divisão inteira é {} e a potência é {}'.format(di, e))
