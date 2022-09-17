menorPeso = 0
maiorPeso = 0

for cont in range(0, 6):
    pesoAtual = float(input('Informe um peso: '))

    if cont == 0:
        maiorPeso = pesoAtual
        menorPeso = pesoAtual
    else:
        if pesoAtual > maiorPeso:
            maiorPeso = pesoAtual
        elif pesoAtual < menorPeso:
            menorPeso = pesoAtual

print('O maior peso foi {}Kg, enquanto o menor foi {}Kg.'.format(maiorPeso, menorPeso))
