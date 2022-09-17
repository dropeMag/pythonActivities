soma = 0

for cont in range(0, 6):
    num = int(input('Insira um número inteiro: '))
    if num % 2 == 0:
        soma += num

print('A soma dos valores pares inseridos é de {}'.format(soma))
