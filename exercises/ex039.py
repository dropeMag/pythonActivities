from random import randint

print('[1] Pedra')
print('[2] Papel')
print('[3] Tesoura')
opcUser = int(input('Esolha: '))
opcComp = randint(1, 3)

if opcComp == 1 and opcUser == 3 or opcComp == 2 and opcUser == 1 or opcComp == 3 and opcUser == 2:
    print('Você perdeu!')
elif opcUser == 1 and opcComp == 3 or opcUser == 2 and opcComp == 1 or opcUser == 3 and opcComp == 2:
    print('Você Ganhou!')
elif opcUser == opcComp:
    print('Empate!')
