print('-=-'*20)
print('ANALISADOR DE TRIÂNGULOS')
print('-=-'*20)

r1 = float(input('Informe o comprimento da primeira reta: '))
r2 = float(input('Informe o comprimeto da segunda reta: '))
r3 = float(input('Informe o comprimento da terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('É POSSÍVEL formar um triângulo com essas três retas.')
    if r1 == r2 == r3 :                                 # todos são iguais
        print('O triângulo formado será EQUILÁTERO.')
    elif r1 != r2 != r3:                                # nenhum lado igual
        print('O trinângulo formado será ESCALENO.')
    else:                                               # 2 lados iguais
        print('O triângulo formado será ISÓSCELES.')
else:
    print('NÃO é possível formar um trinângulo com essas três retas.')
