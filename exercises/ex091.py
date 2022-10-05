from random import randint
from time import sleep
numeros = list()


def sorteia():
    for c in range(0, 5):
        numeros.append(randint(0, 100))


def somaPar(valores):
    somatorio = 0
    for c in valores:
        if c % 2 == 0:
            somatorio += c
    return somatorio


print('Números sorteados: ')
sorteia()
for n in numeros:
    sleep(.5)
    print(n, end=' ')

print('\n')
print('Soma dos números pares:')
total = somaPar(numeros)
print(total)
