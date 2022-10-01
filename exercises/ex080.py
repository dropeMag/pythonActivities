from random import randint
from time import sleep

mega = []
sorteados = list()

print('='*31)
jogos = int(input('Quanto jogos você gostaria? '))

for cont in range(0, jogos):
    for qntJogos in range(0, 6):
        num = randint(1, 60)

        while num in sorteados:
            num = randint(1, 60)

        sorteados.append(num)

    mega.append(sorteados[:])
    sorteados.clear()

print('\n{:-^31}\n'.format(f'SORTEANDO {jogos} JOGOS'))

for numJogo, jogosSort in enumerate(mega):
    print(f'Jogo {numJogo+1}: {sorted(jogosSort)}')
    sleep(1)
