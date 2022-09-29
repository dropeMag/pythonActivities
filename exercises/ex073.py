cont = val5 = 0
numeros = []

while True:
    num = int(input('Informe um valor: '))
    numeros.append(num)

    cont += 1

    if num == 5:
        val5 += 1

    resp = input('Quer continuar? [S/N] ').lower().strip()

    while resp not in 'sn':
        resp = input('Resposta inválida! Responda novamente: [S/N] ')

    if resp == 'n':
        break

numeros.sort(reverse=True)

print(f'\nForam digitados {cont} números.')
print(f'A ordem decrescente da lista é {numeros}')
print(f'Foram digitados {val5} números 5.')
