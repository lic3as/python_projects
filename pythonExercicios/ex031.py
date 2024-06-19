km = int(input('Informe a distância da viagem em km: '))

if km <= 200:           # para viagens de até 200km, o preço é R$0.50 por km
    print('O preço da passagem é R${}'.format(km * 0.5))
else:                  # para viagens maiores, o preço é R$0.45 por km
    print('O preço da passagem é R${}'.format(km * 0.45))
