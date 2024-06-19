velocidade = int(input('Informe a velocidade do carro: '))

if velocidade > 80:                                                         # se a velocidade for maior que 80km/h, o carro é multado
    print('Você foi multado por excesso de velocidade!')                    # imprimir mensagem de multa
    print('O valor da multa é de R${:.2f}'.format((velocidade - 80) * 7))       # multa = R$7 por cada km acima do limite
print('Tenha um bom dia e dirija com segurança!')                           # imprimir bom dia independente da situação
