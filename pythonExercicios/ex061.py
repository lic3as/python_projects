print('=' * 35)
print('GERADOR DE PA')
print('=' * 35)

primeiro = int(input('Primeiro termo: '))       # primeiro termo
razao = int(input('Razão: '))                   # pulando de razão em razão
termo = primeiro                                # armazenar cada termo
count = 1                                       # contador de termos
while count <= 10:                              # enquanto o termo não passar de 10
    print('{}'.format(termo), end=' ->> ')
    termo += razao                              # somar a razão ao termo
    count += 1                                  # incrementar o contador
print('fim')
