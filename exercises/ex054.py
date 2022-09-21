result = 1

num = int(input('Informe um número para fatorar: '))
cont = num

while cont >= 1:
    result *= cont
    cont -= 1

print('O resultado da fatoração de {} é igual a {}'.format(num, result))
