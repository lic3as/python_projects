nome = str(input('Digite o seu nome: '))

if nome == 'Alice':                                 # se nome for igual a Alice
    print('Que nome mais lindo!')                   # somente essa parte identada entrará na condição
else:                                               # senão (lembrar das identações para funcionar
    print('Desculpa, mas Alice é mais bonito...')   # somente essa parte identada entrará na condição
print('É um prazer, {}!'.format(nome))              # essa parte não entrará na condição, ou seja, executará para qualquer nome
