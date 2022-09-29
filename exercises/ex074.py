listaG = []
listaP = []
listaI = []

for c in range(1, 11):
    num = int(input((f'Informe o {c}º número: ')))

    listaG.append(num)

    if num % 2 == 0:
        listaP.append(num)
    else:
        listaI.append(num)

print(f'A lista geral: {listaG}')
print(f'A lista dos pares: {listaP}')
print(f'A lista dos ímpares: {listaI}')
