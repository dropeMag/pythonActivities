galera = []
dado = list()

for c in range(0, 4):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
    print('')

for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')
