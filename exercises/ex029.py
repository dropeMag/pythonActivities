numMenor = float(input('Insira o 1º número: '))
numMaior = numMenor
num2 = float(input('Insira o 2º número: '))

if num2 > numMaior:
    numMaior = num2

if num2 < numMenor:
    numMenor = num2

num3 = float(input('Insira o 3º número: '))

if num3 > numMaior:
    numMaior = num3

if num3 < numMenor:
    numMenor = num3

print('O menor número foi {} e o maior foi {}'.format(numMenor, numMaior))
