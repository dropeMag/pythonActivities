from datetime import date


def voto(i):
    if 16 <= i < 18 or i >= 60:
        return 'Opcional'
    elif i >= 18:
        return 'Obrigatório'
    else:
        return 'Negado'


anoAtual = date.today().year

print('_' * 35)
anoNasc = int(input('Em que ano você nasceu? '))
idade = anoAtual - anoNasc
resp = voto(idade)

print(f'Com {idade} anos, seu voto é {resp}')
