from random import randint
respComp = randint(1, 10)

print('='*8, 'ADIVINHA OU PERCA',  '='*8)

print('\nEM QUE NUMERO ESTOU PENSANDO AGORA?')
respUser = int(input('resposta: '))

while not respUser == respComp:
    print('\nRESPOSTA ERRADA!! TENTE NOVAMENTE!!')
    respUser = int(input('resposta: '))

print('\nPARABÉNS!! VOCÊ ACERTOU!! ERA O {}!!'.format(respComp))
