situ = str()

nome = str(input('Nome do aluno: '))
media = float(input(f'Média de {nome}: '))

if media >= 7:
    situ = 'Aprovado'
else:
    situ = 'Reprovado'

aluno = {'Nome': nome, 'Média': media, 'Situação': situ}
print('='*30)
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
