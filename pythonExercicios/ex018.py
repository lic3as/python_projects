from math import radians, cos, sin, tan

angulo = float(input('Digite o valor ângulo: '))

print('O ângulo de {:.2f}° equivale a {:.2f}rad'.format(angulo, radians(angulo)))   # radians converte graus pra radianos
print('O cosseno desse ângulo vale {:.2f}rad'.format(cos(radians(angulo))))               # calculando o cosseno do ângulo convertido pra radianos
print('O seno desse ângulo vale {:.2f}rad'.format(sin(radians(angulo))))                  # calculando o seno do ângulo convertido pra radianos
print('A tangente desse ângulo vale {:.2f}rad'.format(tan(radians(angulo))))              # calculando a tangente do ângulo convertido pra radianos
