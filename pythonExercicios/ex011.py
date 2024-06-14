l = float(input('Digite a largura da parede: '))
h = float(input('Digite a altura da parede: '))

area = l * h    # área da parede
tinta = area / 2    # cada litro de tinta, pinta 2m^2 de parede

print('Para uma parede de {} metros quadrados, são necessários {} litros de tinta'.format(area, tinta))
