while True:
    n = int(input('Qual a tabuada desejada? '))

    if n <= 0:
        break

    for cont in range(1, 11):
        print(f'{n} x {cont:2} = {n*cont}')

print('Até mais! Obrigado por usar nosso sistema!')
