dist = float(input('Qual a distância da viagem (em Km)? '))

if dist<201:
    valor = dist*0.5
    print('O valor da passagem é de R$ {:.2f}'.format(valor))
else:
    valor = dist*0.45
    print('O valor da passagem é de R$ {:.2f}'.format(valor))
