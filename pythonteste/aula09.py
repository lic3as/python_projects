frase = 'Curso em Vídeo Python'

print(frase)                    # mostrar a frase inteira
print(frase[9])                 # mostrar a frase na posição 9
print(frase[6:14])              # mostrar a frase da posiçao 6 a 13 (terminar em uma antes da última)
print(frase[:15:2])             # mostra do início até o 14 pulando de 2 em 2
print(frase[2:])                # mostrar da posição 2 até o final
print("""Nessa aula, vamos aprender operações com String no Python.
As principais operações que vamos aprender são o Fatiamento de String, 
Análise com len(), count(), find(), transformações com replace(), upper(), 
lower(), capitalize(), title(), strip(), junção com join().""")     # """ servem para imprimir da forma que o texto está formatado no código
print(frase.count('o'))         # contar as ocorrências de 'o' na frase (3)
print(frase.upper().count('o')) # contar as ocorrêcias de 'o' após tornar a frase toda maiúscula (0)
# upper - tornar maiúscula, lower - tornar minúscula, title - tornar a primeira e as letras após os espaços maiúsculas
# capitalize - tornar somente a primeira letra maiúscula, split - fatiar string, strip - tirar so espaços sobrando ao redor
# a maioria dos comandos pode ser utilizado com um r antes para ser feito só na direita ou com um l para só na esquerda
print(len(frase))               # tamanho de frase
print(frase.replace('Python', 'Android'))
# o replace troca o primeiro argumento pelo segundo, ele mesmo adiciona ou remove os caracteres necessários para a mudança
print(frase)                    # provando que a frase só é modificada no momento em que o métodos foi chamado, a string continua a mesma
print('Curso' in frase)         # dizer se a string está ou não presente na frase
print(frase.find('Vídeo'))      # mostrar em qual posição inicia a string 'Vídeo'
print(frase.split())            # mostrar as palavras da frase separadamente em uma lista 
