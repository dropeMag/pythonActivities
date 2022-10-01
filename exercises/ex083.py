from random import randint

jogo = list()

print('Valores sorteados:')
for c1 in range(1, 5):
    valor = randint(1, 6)
    sorteio = {'Jogador': c1, 'Valor': valor}
    jogo.append(sorteio.copy())
    print(f'o jogador{c1} tirou {valor}')

print('\nRanking dos jogadores:')
for c2 in range(0, 4):
    print(f'{c2+1}º lugar: jogador{jogo[c2]["Jogador"]} com {jogo[c2]["Valor"]}')
