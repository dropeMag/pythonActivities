pessoa = list()
grupo = list()
maiPeso = menPeso = 0
maiNome = menNome = str('')

while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))

    grupo.append(pessoa[:])
    pessoa.clear()

    resp = str(input('Quer continuar? [S/N] '))

    while resp not in 'sSnN':
        resp = str(input('[ERROR] Quer continuar? [S/N] '))

    if resp.lower() == 'n':
        break

for p in grupo:
    if p == grupo[0]:
        maiPeso = menPeso = p[1]
        maiNome = menNome = p[0]
    elif p[1] > maiPeso:
        maiPeso = p[1]
        maiNome = p[0]
    elif p[1] < menPeso:
        menPeso = p[1]
        menNome = p[0]

print('-='*30)
print(f'Ao todo foram cadastrados {len(grupo)} pessoas.')
print(f'A pessoa mais pesada é {maiNome}, com {maiPeso:.1f}Kg.')
print(f'A pessoa menos pesada é {menNome}, com {menPeso:.1f}Kg.')
