matriz = []
linha = []
somaGeral = mai2 = tot3l = 0

for lin in range(1, 4):
    for col in range(1, 4):
        num = int(input(f'Linha {lin}, Coluna {col}: '))
        linha.append(num)

        if num % 2 == 0:
            somaGeral += num

        if lin == 2:
            if num > mai2:
                mai2 = num
        elif lin == 3:
            tot3l += num

    matriz.append(linha[:])
    linha.clear()

print('-='*30)

for c1 in matriz:
    print(f'[{c1[0]: ^5}] [{c1[1]: ^5}] [{c1[2]: ^5}]')

print(f'\nA soma de todos os pares é {somaGeral}')
print(f'O maior valor da 2ª linha é {mai2}')
print(f'A soma dos números da 3ª linha é {tot3l}')
