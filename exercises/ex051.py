print('Olá (todo) Mundo! Nos informe seu sexo, por favor.\n[M] ou [F]')
sexo = input('R: ').strip().upper()

while sexo != 'M' and sexo != 'F':
    print('Resposta inválida! Responda novamente!')
    sexo = input('R: ').strip().upper()

print('Obrigado por participar!')
