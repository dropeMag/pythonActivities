from random import shuffle
a1 = input('Nome do 1º aluno: ')
a2 = input('Nome do 2º aluno: ')
a3 = input('Nome do 3º aluno: ')
a4 = input('Nome do 4º aluno: ')

alunos = [a1, a2, a3, a4]
random.shuffle(alunos)

print('A ordem de alunos sorteados é: {}'.format(alunos))
