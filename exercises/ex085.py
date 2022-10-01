"""totGols = 0

jogador = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {jogador} jogou? '))

fichaJogador = {'Nome': jogador, 'Partidas': partidas}

print('')
for cont in range(1, partidas+1):
    gols = int(input(f'Gols feitos na {cont}ª partida: '))
    totGols += gols

    fichaJogador[f'Jogo{cont}'] = gols

fichaJogador['Total'] = totGols

print('-'*30)
for k, v in fichaJogador.items():
    print(f'{k}: {v}')"""

listaGols = list()
totGols = 0

jogador = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {jogador} jogou? '))

fichaJogador = {'Nome': jogador}

for cont in range(1, partidas+1):
    gols = int(input(f'Gols feitos na {cont}ª partida: '))
    totGols += gols
    listaGols.append(gols)

fichaJogador['Gols'] = listaGols[:]
fichaJogador['Total'] = totGols

print('-'*70)
print(fichaJogador)
print('-'*70)
for k, v in fichaJogador.items():
    print(f'{k}: {v}')
print('-'*70)
print(f'O jogador {jogador} jogou {partidas} partidas:')
for num in listaGols:
    print(f'   -> Na partida {listaGols.index(num)+1} fez {num} gol(s).')
print(f'Foi um total de {totGols} gols')
