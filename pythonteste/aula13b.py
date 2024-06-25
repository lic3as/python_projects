print({'=' * 5 + ' CONTAGEM ' + '=' * 5})

inicio = int(input('Informe o valor de INÍCIO: '))
fim = int(input('Informe o valor de FIM: '))
passo = int(input('Informe o valor de PASSO: '))

for contagem in range(inicio, fim + 1, passo):      # contagem começando de início, até fim + 1 (valor de fim) pulando de passo em passo
    print(contagem, end=' ')                        # mostrar os valores separados por espaço
print('')                                           # quebra de linha
print('FIM')
