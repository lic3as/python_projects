nome = str(input('Digite o nome completo: ')).strip()       # já remover os espaços antes e depois

separados = nome.split()        # lista dos nomes separados

print('Primeiro nome: {}'.format(separados[0]))             # mostrar primeiro elemento da lista
print('Último nome: {}'.format(separados[len(separados) - 1]))    # mostrar último elemento (tamanho - 1)
