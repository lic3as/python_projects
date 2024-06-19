print('-=-'*20)                     # estilizar com 20 vezes o -=-
print('ANALISADOR DE TRIÂNGULOS')
print('-=-'*20)

r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))

# para 3 retas formarem um retângulo, a soma de 2 é sempre menor que a terceira
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('É POSSÍVEL formar um triângulo com essas três retas')
else:
    print('NÃO é possível formar um triângulo com essas retas')
