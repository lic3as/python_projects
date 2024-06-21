print('='*15 + ' LOJAS ALICE ' + '='*15)
preco = float(input('Informe o preço das compras: R$'))

print('''FORMAS DE PAGAMENTO:
[1] à vista (dinheiro / pix)
[2] à vista (cartão de débito)
[3] 2x sem juros (cartão de crédito)
[4] 3x ou mais com juros (cartão de crédito)''')
pg = int(input('Qual a forma de pagamento? '))

if pg == 1:         # à vista: 10% de desconto
    novo = preco - (preco * (10/100))       # novo preço = preço - 10%
    print('As compras, com 10% de desconto, vão custar R${:.2f}.'.format(novo))
elif pg == 2:       # débito: 5% de desconto
    novo = preco - (preco * (5/100))        # novo preço = preço - 5%
    print('As compras, com 5% de desconto, vão custar R${:.2f}.'.format(novo))
elif pg == 3:       # 2x no crédito: preço normal
    print('As compras continuam com o mesmo preço, R${:.2f}.'.format(preco))
    print('As 2 parcelas custarão R${:.2f}.'.format(preco/2))                       # 2 parcelas
elif pg == 4:       # 3x ou mais no crédito: 20% de juros
    novo = preco + (preco * (20/100))       # novo preço = preço + 20%
    print('As compras, com 20% de juros, vão custar R${:.2f}.'.format(novo))
    parc = int(input('Em quantas parcelas deseja efetuar o pagamento? '))
    print('As {} parcelas custarão R${:.2f}.'.format(parc, novo/parc))      # qtd de parcelas e preço das parcelas
else:               # nenhuma das opções
    print('\033[31mOperação não suportada.\033[m')
