from datetime import date

anoAtual = date.today().year
maioridade = anoAtual - 18
numAdultos = 0

for cont in range(1, 8):
    anoNasc = int(input('Escreva o ano de nascimento da {}ª pessoa: '.format(cont)))
    if anoNasc <= maioridade:
        numAdultos += 1

print('\nO número aproximado de maiores de idade é de {} pessoas'.format(numAdultos))
