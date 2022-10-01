turma = []

while True:
    nome = str(input('Nome: '))
    nt1 = float(input('Nota 1: '))
    nt2 = float(input('Nota 2: '))
    media = (nt1 + nt2)/2

    turma.append([nome, [nt1, nt2], media])

    continuar = str(input('Continuar? [S/N] ')).strip()

    if continuar[0] in 'nN':
        break

print('-'*60)
print('{:<4}{:<11}{}'.format('No.', 'NOME', 'MÉDIA'))
print('-'*20)

for numAlunos in turma:
    print('{:<4}{:<11}{:>5.1f}'.format(turma.index(numAlunos), numAlunos[0], numAlunos[2]))

while True:
    print('-' * 60)
    resp = int(input('Mostrar notas de qual aluno? [999 para parar]'))

    if resp == 999:
        break

    print(f'As notas de {turma[resp][0]} são: {turma[resp][1]}')

print('-' * 60)
print('{: ^31}'.format('OBRIGADO POR USAR NOSSO SISTEMA!'))
