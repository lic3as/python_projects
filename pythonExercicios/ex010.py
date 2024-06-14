real = float(input('Quanto de dinheiro você tem na carteira? '))

dolar = real / 3.27   # considerando US$1,00 = R$3,27

print('Com R${}, você pode comprar US${}'.format(real, dolar))
