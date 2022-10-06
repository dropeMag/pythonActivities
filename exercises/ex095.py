def leiaInt(n):
    if n.isnumeric():
        print(f'Você digitou o valor {n}')
        return True
    else:
        print('[ERRO] INSIRA UM VALOR NUMÉRICO INTEIRO!')


# Programa Principal
while True:
    num = leiaInt(input('Digite um número: '))
    if num:
        break
