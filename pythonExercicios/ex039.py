from datetime import date

nasc = int(input('Informe o ano do seu nascimento: '))

idade = date.today().year - nasc            # pegar o ano atual e diminuir o ano de nascimento para saber a idade

if idade < 18:                              # se menor que 18, ainda vai se alistar
    print('Ainda faltam {} anos para o alistamento.'.format(18 - idade))            # quantos anos faltam pros 18
    print('Seu alistamento será em {}.'.format(nasc + 18))                           # ano que ele terá 18 anos
elif idade > 18:                            # senão, se maior que 18, está atrasado
    print('Você já deveria ter se alistado há {} anos.'.format(idade - 18))         # quantos anos excedem os 18
    print('Seu alistamento foi em {}.'.format(nasc + 18))                            # ano que ele tinha 18 anos
else:                                       # senão, é hora de se alistar (18 anos)
    print('Você tem que se alistar IMEDIATAMENTE!')
