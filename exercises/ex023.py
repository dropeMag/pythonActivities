n1 = float(input('Digita a primeira nota: '))
n2 = float(input('Digita a segunda nota: '))
media = (n1+n2)/2

print('A sua média foi: {}'.format(media))

"""if media>=6:
    print('Parabéns, você passou!')
else:
    print('Que pena... Estude mais!')"""

print('Parabéns, você passou!' if media>=6 else'Que pena... Estude mais!')
