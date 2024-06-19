num = int(input('Digite um número de 0 a 9999: '))

milhar = num // 1000                # descobrir a quantidade de milhares
num = num - milhar * 1000           # tirar os milhares pra calcular as centenas
centena = num // 100                # descobrir a quantidade de centenas
num = num - centena * 100           # tirar as centenas pra calcular as dezenas
dezena = num // 10                  # descobrir a quantidade de dezenas
num = num - dezena * 10             # tirar as dezenas pra calcular as unidades
unidade = num // 1                  # descobrir a quantidade de unidades, não precisa diminuir depois porque já chegamos ao fim do número

print('Milhar: {}'.format(milhar))
print('Centena: {}'.format(centena))
print('Dezena: {}'.format(dezena))
print('Unidade: {}'.format(unidade))
