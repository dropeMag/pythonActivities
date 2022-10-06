def ficha(nome="<desconhecido>", gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


# Programa Principal
n = str(input('Nome do Jogador: ')).strip()
g = str(input('Número de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0

if len(n) == 0:
    ficha(gols=g)
else:
    ficha(n, g)