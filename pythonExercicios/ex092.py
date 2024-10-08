# 35 anos de contribuição para se aposentar
# calcular a idade a partir do ano de nascimento e guardar isso (nome, idade e carteira de trabalho)
# se a carteira de trabalho for igual0, não tem
# se tiver carteira de trabalho, pergunta o ano de contratação e o salário
# calcular a idade que a pessoa precisará pra poder se aposentar

from datetime import datetime
carteira = dict()
carteira['Nome'] = str(input('Nome: '))
anoNasc = int(input('Ano de Nascimento: '))
carteira['Idade'] = datetime.now().year - anoNasc                                          # calcular a idade
carteira['CTPS'] = int(input('Carteira de Trabalho (0 = não tem): '))

if carteira['CTPS'] == 0:                                                   # se não tiver carteira, só imprime os dados
    print(carteira)
    for k, v in carteira.items():
        print(f'{k} tem o valor {v}')
else:                                                                       # se tiver carteira
    carteira['Contratação'] = int(input('Ano de Contratação: '))
    carteira['Salário'] = float(input('Salário: R$ '))
    anosTrabalhados = 2024 - carteira['Contratação']                        # anos trabalhados
    carteira['Aposentadoria'] = carteira['Idade'] + (35 - anosTrabalhados)  # a idade aposentadoria é a idade mais os anos que ainda precisam ser trabalhados pra totalizar 35
    #imprimir:
    print(carteira)
    for k, v in carteira.items():
        print(f'{k} tem o valor {v}')