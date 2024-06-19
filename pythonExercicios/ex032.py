from datetime import date                                       # pegar o ano atual

ano = int(input('Qual ano você quer analisar? Digite 0 para o ano atual... '))
if ano == 0:                                                    # se digitar 0, pegar o valor do ano atual
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:           # se o ano obedecer a essas condições, ele é bissexto
    print('O ano {} é BISSEXTO!'.format(ano))
else:                                                           # senão, ele não é
    print('O ano {} NÃO é bissexto'.format(ano))
