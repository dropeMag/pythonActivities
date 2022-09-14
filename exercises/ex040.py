num = int(input('Insira um número inteiro: '))
print('''Escolha uma das opções:
[ 1 ] converter para Binário
[ 2 ] converter para Octal
[ 3 ] converter para Hexadecimal''')

opc = int(input('Sua opção: '))

if opc == 1:
    print('O valor {} em Binário é igual a {}'.format(num, bin(num)))
elif opc == 2:
    print('O valor {} em Binário é igual a {}'.format(num, oct(num)))
elif opc == 3:
    print('O valor {} em Binário é igual a {}'.format(num, hex(num)))
else:
    print('Opção Inválida!')
