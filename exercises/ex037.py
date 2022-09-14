userAlt = float(input('Informe sua altura (em metros): '))
userPeso = float(input('Informe seu peso (em Kg): '))

imc = userPeso / (userAlt ** 2)

if imc <= 18.5:
    status = 'abaixo do peso'
elif imc > 18.5 and imc <= 25:
    status = 'peso ideal'
elif imc > 25 and imc <= 30:
    status = 'sobrepeso'
elif imc > 30 and imc <= 40:
    status = 'obesidade'
else:
    status = 'obesidade morbida'

print('Usuário, seu status é: {}!'.format(status))
