print('-' * 50)
print('BANCO BRADESCO')
print('-' * 50)

saque = int(input('Qual valor você quer sacar? R$ '))

cedula = 50                             # iniciando com a cédula de 50
totCedula = 0                           # total de cada cédula
while True:                             # loop infinito
    if saque >= cedula:                 # se a cedula for menor que o saque
        saque -= cedula                 # tira o total de uma cédula
        totCedula += 1                  # aumenta a quantidade de cédulas
    else:                               # se o saque for menor que a cédula atual, troca
        if totCedula > 0:               # só informa o total de cédula se ele for maior que 0
            print(f'Total de {totCedula} cédulas de R$ {cedula}.')
        if cedula == 50:                # se for 50, troca pra 20 e zera totCedula
            cedula = 20
            totCedula = 0
        elif cedula == 20:              # se for 20, troca por 10 e zera totCedula
            cedula = 10
            totCedula = 0
        elif cedula == 10:              # se for 10, troca por 1 e zera totCedula
            cedula = 1
            totCedula = 0
        if saque == 0:                  # quando terminar o dinheiro, para
            break

print('-' * 50)
print(f'Volte sempre!')
