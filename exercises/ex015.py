import math
ctt1 = float(input('Informe o valor do cateto oposto: '))
ctt2 = float(input('Informe o valor do cateto adjacente: '))
hipo = math.sqrt(math.pow(ctt1, 2) + math.pow(ctt2, 2))
# hipo = math.hypot(ctt1, ctt2)

print('A hipotenusa do triângulo com catetos {} e {} vale {}'.format(ctt1, ctt2, hipo))
