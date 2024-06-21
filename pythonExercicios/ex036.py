print('-=-'*20)
print('PROGRAMA DE EMPRÉSTIMO')
print('-=-'*20)

casa = float(input('Digite o valor da casa a ser comprada: R$'))
salario = float(input('Digite o valor do seu salário atual: R$'))
anos = int(input('Em quantos anos de financiamento você deseja pagar? '))

prestacao = casa / (12 * anos)                          # a prestação mensal será o valor da casa dividida pelos meses de cada ano de pagamento -> 1 ano = 12 meses
print('O custo de prestação mensal da sua casa será de R${:.2f}'.format(prestacao))

if salario * (30/100) >= prestacao:                      # aprovar apenas se a prestação não exceder 30% do salário
    print('Parabéns! O seu empréstimo foi APROVADO.')
else:
    print('O seu empréstimo foi NEGADO. A prestação da casa excede 30% do seu salário. Sentimos muito.')
