km = int(input('Quantos km foram percorridos com o carro? '))
dias = int(input('Por quantos dias o carro foi alugado? '))

preco = (60 * dias) + (0.15 * km)   # o preço é R$60 por dia e R$0.15 por km rodado

print('O total a pagar por {} km rodados e {} dias alugados é R${}'.format(km, dias, preco))
