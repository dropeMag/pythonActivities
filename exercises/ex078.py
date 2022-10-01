numeros = [[], []]

for c1 in range(1, 8):
    num = int(input(f'Informe o {c1}º valor: '))

    if num % 2 == 0:
        numeros[0].append(num)
    elif num % 2 != 0:
        numeros[1].append(num)

print(f'Os valores pares são: {sorted(numeros[0])}')
print(f'Os valores impares são: {sorted(numeros[1])}')
