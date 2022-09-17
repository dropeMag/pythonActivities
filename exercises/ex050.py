idadeVelho = 0
mulheresNovas = 0
somaIdades = 0

print('PESQUISA IBGE:')

for cont in range(1, 5):
    nome = input('\nEscreva o nome da {}ª pessoa: '.format(cont))
    idade = int(input('Escreva a idade de {}: '.format(nome)))
    sexo = input('Escreva o sexo de {} [M] ou [F]: '.format(nome)).lower()

    if idade > idadeVelho and sexo == 'm':
        idadeVelho = idade
        nomeVelho = nome

    if sexo == 'f' and idade < 20:
        mulheresNovas += 1

    somaIdades += idade

print('A média de idade do grupo é de {:.0f} anos'.format(somaIdades/4))
print('No grupo, há {} mulhere(s) com menos de 20 anos'.format(mulheresNovas))
print('O homem mais velho do grupo se chama {}'.format(nomeVelho))
