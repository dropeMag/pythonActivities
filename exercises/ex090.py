valores = list()


def maior(val):
    numMaior = 0
    for cont in val:
        if val.index(cont) == 0:
            numMaior = cont
        else:
            if cont > numMaior:
                numMaior = cont
        cont += 1
    print(f'O maior número foi {numMaior}')


while True:
    num = int(input('Informe um valor [negativo para parar]: '))

    if num < 0:
        break

    valores.append(num)

maior(valores)
