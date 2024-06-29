print('-' * 40)
print('SEQUÊNCIA DE FIBONACCI')
print('-' * 40)

n = int(input('Quantos termos você quer mostrar? '))

f1 = 0                      # primeiro fibonacci é 0
f2 = 1                      # segundo fibonacci é 1
print('{} -> {} -> '.format(f1, f2), end='')

while n > 2:                # enquanto não chegar nos 2 primeiros
    aux = f1                # guardar valor do f1
    f1 = f2                 # atualizar f1 pra f2
    f2 += aux               # adidionar f1 a f2
    print('{} -> '.format(f2), end='')
    n -= 1                  # decrementa n
print('FIM')
