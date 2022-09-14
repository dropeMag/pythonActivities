import datetime
anoNasc = int(input('Informe o seu ano de nascimento: '))
anoAtual = datetime.date.today().year

iddUser = anoAtual - anoNasc

if iddUser < 18:
    print('Ainda não está na hora de você se alistar no exército!')
    print('Ainda falta {} anos!'.format(18-iddUser))
elif iddUser == 18:
    print('Esse ano você deve se apresentar para o alistamento militar!')
elif iddUser > 18:
    print('Já passou da época de você se alistar no exército!')
    print('Se ainda não se alistou, aliste-se o mais rápido possível!')
    print('Já se passaram {} anos desde o dia de apresentação!'.format(iddUser-18))
