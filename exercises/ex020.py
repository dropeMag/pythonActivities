valor = input('Informe um valor de 0 a 9999: ')
rolav = valor[::-1]

print('Unidade: {}'.format(rolav[0].replace(' ', '0')))
print('Dezena: {}'.format(rolav[1].replace(' ', '0')))
print('Centena: {}'.format(rolav[2].replace(' ', '0')))
print('Milhar: {}'.format(rolav[3].replace(' ', '0')))
