valCasa = float(input('Qual o valor da casa? R$ '))
salComp = float(input('Qual o seu salário? R$ '))
qtdAnos = int(input('Em quantos anos ocê irá pagar? '))

prtMens = valCasa / (qtdAnos * 12)
salPorc = (salComp * 30) / 100

if prtMens >= salPorc:
    print('O valor mensal da prestação será de R$ {:.2f}'.format(prtMens))
    print('Desulpe, seu empréstimo foi negado!')
else:
    print('O valor mensal da prestação será de R$ {:.2f}'.format(prtMens))
    print('Parabéns, seu empréstimo foi aprovado!')
