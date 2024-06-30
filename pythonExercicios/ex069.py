maiores = homens = mulheres20 = 0
sexo = 's'
continuar = 'c'
while True:                                 # loop infinito
    print('-' * 50)
    print('CADASTRE UMA PESSOA')
    print('-' * 50)
    idade = int(input('Informe a idade da pessoa: '))
    while sexo not in 'FM':                 # fazer a validação
        sexo = str(input('Informe o sexo da pessoa [F/M]: ')).strip().upper()[0]
    if idade > 18:                          # se for maior de 18, incrementa maiores
        maiores += 1
    if sexo == 'M':                         # se for homem, incrementa homens
        homens += 1
    if sexo == 'F' and idade < 20:          # se for mulher e menor de 20, incrementa mulheres20
        mulheres20 += 1
    print('-' * 50)
    while continuar not in 'SN':            # fazer a validação
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        print('-' * 50)
        print(f'{maiores} pessoas maiores de 18 anos foram cadastradas.')
        print(f'{homens} homens foram cadastrados.')
        print(f'{mulheres20} mulheres com menos de 20 anos foram cadastradas.')
        break
