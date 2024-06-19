cidade = str(input('Digite o nome de uma cidade: ')).split()        # já remover os espaços ao redor

cidade = cidade.upper()              # colocar em maiúsculo pra que funcione sem case sensitive
espaco = cidade.find(' ')            # encontrar o fim do primeiro nome

print('Essa cidade começa com a palavra "Santo"? {}'.format('SANTO' in cidade[:espaco]))
