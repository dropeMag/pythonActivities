numExt = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')

while True:
    escolha = int(input('Escolha um número entre 0 e 10: '))

    if escolha in range(0, len(numExt)):
        print(f'Você escolheu o número {numExt[escolha]}.')
        break

    print('[ERRO]', end=' ')
