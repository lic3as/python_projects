print('=' * 35)
print('10 TERMOS DE UMA PA')
print('=' * 35)

primeiro = int(input('Primeiro termo: '))       # primeiro termo
razao = int(input('Razão: '))                   # pulando de razão em razão
decimo = primeiro + (10 - 1) * razao            # décimo termo para saber em qual parar

for termo in range(primeiro, decimo + razao, razao):    # começando do primeiro termo, pulando o valor da razão e parando no décimo primeiro termo (encontrado com a fórmula + razão)
    print('{}'.format(termo), end=' ->> ')
print('fim')
