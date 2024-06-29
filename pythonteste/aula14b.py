resposta = 'S'                                                      # condição de parada (se não for sim, ele para o programa)

while resposta in 'S':                                              # enquanto a resposta for sim
    num = int(input('Informe um número: '))                         # informa um número
    resposta = str(input('Deseja continuar? [S/N] ')).upper()       # informa se quer continuar

print('FIM')