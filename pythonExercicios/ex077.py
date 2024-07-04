tupla = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for palavra in tupla:                                               # percorrer a tupla
    print(f'Na palavra {palavra.upper()} temos ', end='')           # imprime as palavras em maiúsculo
    for c in range(0, len(palavra)):                                # percorrer a palavra
        if palavra[c] in 'aeiou':                                   # se a letra da palavra for uma das vogais, imprimir
            print(palavra[c], end=' ')
    print('')
