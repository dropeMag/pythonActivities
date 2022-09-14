nt1 = float(input('Informe a primera nota: '))
nt2 = float(input('Informe a segunda nota: '))

med = (nt1 + nt2)/2

if med >= 7:
    print('Parabéns, você foi aprovado!')
elif med >= 5:
    print('Você está em recuperação!')
else:
    print('Que pena! Você foi reprovado!')
