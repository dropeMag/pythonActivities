continuar = 'S'
while continuar != 'N':
    num = int(input('Qual o número? '))
    raz = int(input('Qual a razão da PA? '))
    termo = num
    cont = int(input('Quantos termos gostaria de ver? '))

    print('\nOs {} primeiros termos dessa progressão são:'.format(cont))
    while cont >= 1:
        print(termo, end=' ')
        termo += num
        cont -= 1

    continuar = input('\n\nGostaria de continuar? [S] [N] ').upper()
    if continuar != 'S' and continuar != 'N':
        print('Resposta inválida!')
        continuar = input('Gostaria de continuar? [S] [N] ').upper()
