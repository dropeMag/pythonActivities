def mensagem():
    print('Impossível realizar contagem!')
    print('Passo inválido!')


def contador(i, f, p):
    if i < f:
        if p > 0:
            while i <= f:
                print(i, end=' ')
                i += p
        elif p < 0 or p == 0:
            mensagem()
        print('')
    elif i > f:
        if p < 0:
            while i >= f:
                print(i, end=' ')
                i += p
        elif p > 0 or p == 0:
            mensagem()
        print('')
    else:
        print('Ambos os números eram o mesmo!')


def titulo(txt):
    print('\n', f'{txt:^22}')
    print('='*24)


numI = int(input('Informe o primeiro valor: '))
numF = int(input('Informe o último valor: '))
numP = int(input('Informe o passo: '))
titulo('CONTAGEM A')
contador(1, 10, 1)
titulo('CONTAGEM B')
contador(10, 0, -2)
titulo('CONTAGEM PERSONALIZADA')
contador(numI, numF, numP)
