soma = 0

for cont in range(1, 500, 2):
    if cont % 3 == 0:
        soma += cont

print('A soma dos ímpares múltiplos de 3 de 1 até 500 é igual a: {}'.format(soma))
