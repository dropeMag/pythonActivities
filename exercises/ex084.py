from datetime import date

nome = str(input('Nome: '))
anoNasc = int(input('Ano de Nascimento: '))
ctps = int(input('Carteira de Trabalho (0 caso não tenha): '))

idade = date.today().year - anoNasc

pessoa = {'Nome': nome, 'Idade': idade, 'CTPS': ctps}

if ctps == 0:
    print('- ' * 80)
    print(pessoa)
    for k, v in pessoa.items():
        print(f'{k}: {v}')
else:
    anoCont = int(input('Ano de Contratação: '))
    salario = float(input('Salário: R$ '))

    aposent = ((anoCont + 32) - date.today().year) + idade

    pessoa['Contratação'] = anoCont
    pessoa['Salário'] = salario
    pessoa['Aposentadoria'] = aposent

    print('- ' * 80)
    print(pessoa)
    for k, v in pessoa.items():
        print(f'{k}: {v}')
