frase = str(input('Digite uma frase: ')).strip()

letras = ''                 # armazenar somente as letras da frase sem os espaços

for c in range(0, len(frase)):
    if frase[c] != ' ':
        letras += frase[c]  # adicionar somente quando for uma letra

contrario = ''              # aramazenar o contrário das letras da frase

for c in range(len(letras) - 1, -1, -1):
    contrario += letras[c]  # pegar as letras de trás pra frente

print('O contrário de {} é {}.'.format(letras.upper(), contrario.upper()))      # mostrar o original e o contrário em maiúsculas

if letras == contrario:
    print('Temos um palíndromo!')
else:
    print('Não temos um palíndromo.')
