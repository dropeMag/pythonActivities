lar = float(input('Qual a largura da parede? '))
alt = float(input('Qual a altura da parede? '))
area = lar*alt

print('Sabendo que cada litro de tinta pinta uma área de 2m quadrados,')
print('serão necessários {:.2f}l para pintar toda a parede!'.format(area/2))
