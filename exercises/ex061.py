mais18 = homens = mulheresJovens = 0
cont = 1

while True:
    userId = int(input(f'Qual a idade do {cont}º usuário? '))
    userSx = input('E qual o sexo? [M/F] ').strip().upper()

    while userSx != 'M' and userSx != 'F':
        print('Sexo inválido! Responda novamente!')
        userSx = input(f'Qual o sexo do {cont}º usuário? [M/F] ').strip().upper()

    if userSx == 'M':
        homens += 1

    if userId > 18:
        mais18 += 1

    if userSx == 'F' and userId < 20:
        mulheresJovens += 1

    cont += 1

    adicionar = input('Deseja continuar? S/N ').strip().upper()

    if adicionar == 'N':
        break

print(f'{mais18} são maiores de 18!')
print(f'{homens} são homens!')
print(f'{mulheresJovens} são mulheres abaixo dos 20!')
