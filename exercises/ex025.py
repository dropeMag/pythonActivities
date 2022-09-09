veloc = float(input('Em qual velocidade estava o veículo? '))

if veloc<81:
    print('O veículo não foi multado!')
else:
    multa = (veloc-80)*7
    print('O veículo foi multado!')
    print('O valor de multa é de R$ {:.2f}'.format(multa))
    