dia = int(input('Quantos dias alugado? '))
kms = float(input('Quantos kms corridos? '))

tot = (60*dia)+(0.15*kms)

print('O total a pagar é de R$ {:.2f}'.format(tot))
