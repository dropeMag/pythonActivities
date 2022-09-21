n1 = int(input('Informe o primeiro valor: '))
n2 = int(input('Informe o segundo valor: '))
resp = int(0)

while resp != 5:
    print('\n O que deseja fazer?:')
    print('[1] somar')
    print('[2] multiplicar')
    print('[3] maior')
    print('[4] novos números')
    print('[5] sair do programa')
    resp = int(input('Resp.: '))

    while resp < 1 and resp > 5:
        print('Resposta inválida! Responda novamente!')
        resp = int(input('Resp.: '))

    if resp == 1:
        print('A soma de {} e {} é igual a {}!'.format(n1, n2, n1+n2))

    if resp == 2:
        print('A multiplicação de {} e {} é igual a {}!'.format(n1, n2, n1*n2))

    if resp == 3:
        if n1 > n2:
            print('O maior número é {}'.format(n1))
        elif n2 > n1:
            print('O maior número é {}'.format(n2))
        else:
            print('Ambos os números são identicos!')

    if resp == 4:
        n1 = int(input('Informe o novo valor de n1: '))
        n2 = int(input('Informe o novo valor de n2: '))

print('Obrigado por usar nosso sistema!')
