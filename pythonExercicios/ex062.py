print('=' * 35)
print('GERADOR DE PA')
print('=' * 35)

primeiro = int(input('Primeiro termo: '))       # primeiro termo
razao = int(input('Razão: '))                   # pulando de razão em razão

termo = primeiro                                # armazenar o valor do termo
count = 0                                       # contador de termos

while count < 10:                               # enquanto o termo for menor que 10
    print('{}'.format(termo), end=' -> ')
    termo += razao                              # somar a razão ao termo
    count += 1                                  # incrementa os termos
print('PAUSA')

mais = 1                                        # quanto quer ver mais
while mais != 0:                                # para quando mais for 0
    mais = int(input('Quer ver mais quantos termos? '))
    aux = 0                                     # contar quantos termos a mais foram mostrados agora
    while aux < mais:                           # enquanto não chegar a quantidade de termos a mais
        print('{}'.format(termo), end=' -> ')
        termo += razao                          # somar a razão ao termo
        count += 1                              # incrementa a quantidade de termos
        aux += 1                                # incrementar a quantidade de mostrados agora
    print('PAUSA')

print('Progressão finalizada com {} termos mostrados.'.format(count))
