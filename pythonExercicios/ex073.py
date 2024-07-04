brasileirao = ('Flamengo', 'Palmeiras', 'Botafogo', 'Bahia',
               'Atlético-PR', 'São Paulo', 'Cruzeiro', 'Fortaleza',
               'Bragantino', 'Internacional', 'Atlético-MG', 'Juventude',
               'Criciúma', 'Cuiabá', 'Vitória', 'Vasco da Gama',
               'Atlético-GO', 'Grêmio', 'Corinthians', 'Fluminense')
# tupla com os 20 primeiros colocados do brasileirão

print('BRASILEIRÃO SÉRIE A:')
for clube in brasileirao:                       # todos os clubes da tupla
    print(clube)

print('-' * 40)
print('PRIMEIROS COLOCADOS DO BRASILEIRÃO:')
for clube in range(0,5):                        # cinco primeiro colocados
    print(brasileirao[clube])

print('-' * 40)
print('ÚLTIMOS COLOCADOS DO BRASILEIRÃO:')
for clube in range(19, 15, -1):                     # quatrp últimos colocados
    print(brasileirao[clube])

print('-' * 40)
print('SÉRIE A EM ORDEM ALFABÉTICA:')           # em ordem alfabética
for clube in sorted(brasileirao):
    print(clube)

print('-' * 40)                                 # posição do são paulo
print(f'O time do São Paulo está na posição {brasileirao.index('São Paulo') + 1}')
