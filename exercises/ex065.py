timesFut = 'Palmeiras', 'Internacional', 'Fluminense', 'Flamengo', 'Corinthians', 'Atlético-PR', 'Atlético-MG', 'América-MG', 'Goiás', 'São Paulo'

print(f'Os 5 primeiros colocados são: {timesFut[0:5]}\n', '- = '*43)
print(f'os 4 últimos colocados são: {timesFut[-4:]}\n', '- = '*43)
print(f'A lista em ordem alfabética fica: {sorted(timesFut)}\n', '- = '*43)
print(f"O time Atlético-PR está em {timesFut.index('Atlético-PR')+1}ª posição")
