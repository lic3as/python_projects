nome = str(input('Digite seu nome completo: ')).strip()         # já vai eliminar os espaços antes e depois

print('Analisando seu nome...')
print('Seu nome em maiúsculas: {}'.format(nome.upper()))
print('Seu nome em minúsculas: {}'.format(nome.lower()))
print('Seu nome completo possui {} letras'.format(len(nome) - nome.count(' ')))             # tamanho do nome menos a quantidade de espaços
nomes = nome.split()            # lista com todos os nomes
print('Seu primeiro nome é {} e possui {} letras'.format(nomes[0], len(nomes[0])))    # primeiro nome e tamanho do primeiro nome presente na lista
