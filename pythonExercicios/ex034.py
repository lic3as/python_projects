salario = float(input('Digite o valor do salário: '))

if salario > 1250:          # se o salário for maior que 1250, o aumento é de 10%
    print('O aumento será de R${:.2f}'.format(salario * (10/100)))
    print('Resultando em R${:.2f}'.format(salario + (salario * (10/100))))
else:                       # senão, o aumento é de 15%
    print('O aumento será de R${:.2f}'.format(salario * (15/100)))
    print('Resultando em R${:.2f}'.format(salario + (salario * (15/100))))
