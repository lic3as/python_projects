num = somaNum = qtdNum = 0      # inicializar as variáveis

while num != 999:               # condição de parada = 999 (flag)
    num = int(input('Informe um número inteiro [999 para parar]: '))
    if num != 999:              # se não for a condição de parada
        somaNum += num          # adiciona num na soma
        qtdNum += 1             # incrementa a quantidade de números
print('Foram digitados {} números e a soma entre eles é {}.'.format(qtdNum, somaNum))
