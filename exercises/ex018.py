import math
ang = float(input('Informe um ângulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))

print('Os seno, cosseno e tangente do ângulo {}º são, respectivamente: {:.2f}, {:.2f} e {:.2f}'.format(ang, sen, cos, tan))
