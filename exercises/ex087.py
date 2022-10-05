def area(lar, com):
    terreno = lar * com
    print(f'A área de um terreno de {lar}x{com} é de {terreno}m²')


larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
area(larg, comp)
