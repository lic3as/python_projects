from math import hypot  # método para calcular a hipotenusa

co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))

# pra calcular a hipotenusa (hip² = co² + ca²) sem importações, era só fazer: hip = (co ** 2 + ca ** 2) ** (1/2)

print('A hipotenusa do triângulo retângulo de cateto oposto {:.2f} e cateto adjacente {:.2f} vale {:.2f}'.format(co, ca, hypot(co, ca)))
