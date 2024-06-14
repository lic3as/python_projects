preco = float(input('Digite o preço do produto: R$'))

descontado = preco - (preco * (5 / 100))    # desconto de 5%

print('Com 5% de desconto, fica por R${}'.format(descontado))
