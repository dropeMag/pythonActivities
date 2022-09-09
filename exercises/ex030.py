salar = float(input('Insira o seu salário: R$ '))

if salar >= 1250:
    salar2 = salar + ((salar * 10) / 100)
    print('Seu novo salário é de R$ {}'.format(salar2))
else:
    salar2 = salar + ((salar * 15) / 100)
    print('Seu novo salário é de R$ {}'.format(salar2))
