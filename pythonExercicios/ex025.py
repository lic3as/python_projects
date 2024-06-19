nome = str(input('Digite o nome completo: ')).strip()               # já remover os espaços entre a string

print('Essa pessoa possui "Silva" no nome? {}'.format('SILVA' in nome.upper()))     # checar sem case sensitive
