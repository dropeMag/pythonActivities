num = int(input('Qual o número? '))
raz = int(input('Qual a razão da PA? '))
ter = num

print('Os 10 primeiros termos dessa progressão são:')
for cont in range(0, 11):
    print('{}'.format(ter), end=' ')
    ter += raz
