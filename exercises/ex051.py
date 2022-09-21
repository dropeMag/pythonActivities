print('Olá (todo) Mundo! Nos informe seu sexo, por favor.\n[M] ou [F]')
sexo = input('R: ').upper()

while sexo != 'M' and sexo != 'F':
    print('Resposta inválida! Responda novamente!')
    sexo = input('R: ').upper()

print('Obrigado por participar!')
