impares = 0

valores = (int(input('Informe o 1º valor: ')),
           int(input('Informe o 2º valor: ')),
           int(input('Informe o 3º valor: ')),
           int(input('Informe o 4º valor: ')))

print(f'O valor 9 apareceu {valores.count(9)} vez(es).')

if 3 not in valores:
    print('O valor 3 não foi digitado.')
else:
    print(f'O 1º valor 3 está na {valores.index(3) + 1}ª posição.')

print('O valores pares digitados foram: ', end='')
for cnt in valores: #você não precisa usar o range, apenas colocar a Tupla
    if cnt % 2 == 0:
        print(cnt, end=' ')
    else:
        impares += 1

    if impares == 4:
        print('Nenhum')

"""
MÉTODO ANTIGO:

n1 = int(input('Informe o 1º valor: '))
n2 = int(input('Informe o 2º valor: '))
n3 = int(input('Informe o 3º valor: '))
n4 = int(input('Informe o 4º valor: '))

valores = n1, n2, n3, n4"""
