import datetime
anoNasc = int(input('Informe seu ano de nascimento: '))
anoAtual = datetime.date.today().year

atletaIdade = anoAtual - anoNasc

if atletaIdade <= 9:
    categ = 'MIRIM'
elif atletaIdade <= 14:
    categ = 'INFANTIL'
elif atletaIdade <= 19:
    categ = 'JÚNIOR'
elif atletaIdade == 20:
    categ = 'SÊNIOR'
else:
    categ = 'MASTER'

print('Idade do atleta: {}'.format(atletaIdade))
print('A categoria do atleta é: {}'.format(categ))
