import random

numUser = int(input('Uusário, informe um número de 0 a 5: '))
numComp = random.randint(0, 5)

if numUser==numComp:
    print('Parabéns usuário, os números são os mesmos!')
else:
    print('Que pena... você escolheu {}, mas o certo era {}!'.format(numUser, numComp))
