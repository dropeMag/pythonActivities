valores = []

while True:
    valor = int(input('Informe um valor: '))
    if valor in valores:
        print(f'O valor já se encontra na lista!')
    else:
        valores.append(valor)

    resp = input('Quer continuar? [S/N] ').strip().lower()

    while resp not in 'ns':
        print('[ERRO] Resposta inválida!')
        resp = input('Quer continuar? [S/N] ').strip().lower()

    if resp == 'n':
        break

print(f'Os valores informados por você foram: {sorted(valores)}')
