expressao = list()

stringExp = str(input('Digite a expressão: '))          # pegar a expressão como uma string
for p in range(0, len(stringExp)):                      # dividir a string para adicionar a lista ((expressao)
    expressao.append(stringExp[p])

parenteses = 0                                          # guardar a quantidade de parênteses
for c in range(0, len(expressao)):                      # percorrer toda a expressão
    if expressao[c] == '(':                             # se for um ( incrementa parenteses
        parenteses += 1
    elif expressao[c] == ')':                           # se for um ) decrementa parenteses
        parenteses -= 1

if parenteses == 0:                                     # se não sobrar nenhum parêntese por fechar, está válida
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
