print('{:=^40}\n{: ^40}\n{:=^40}'.format('', ' BANCO TAMBÉM DO PEDRÃO ', ''))
qnt50 = qnt20 = qnt10 = qnt1 = 0
valor = int(input('Quanto você deseja sacar? R$ '))

while True:
    if valor >= 50:
        valor -= 50
        qnt50 += 1
    else:
        break

while True:
    if valor >= 20:
        valor -= 20
        qnt20 += 1
    else:
        break

while True:
    if valor >= 10:
        valor -= 10
        qnt10 += 1
    else:
        break

while True:
    if valor >= 1:
        valor -= 1
        qnt1 += 1
    else:
        break

if qnt50 != 0:
    print(f'Total de {qnt50} cédulas de R$ 50')
if qnt20 != 0:
    print(f'Total de {qnt20} cédulas de R$ 20')
if qnt10 != 0:
    print(f'Total de {qnt10} cédulas de R$ 10')
if qnt1 != 0:
    print(f'Total de {qnt1} cédulas de R$ 1')

print('{:=^40}\n{: ^40}\n{: ^40}'.format('', ' VOLTE SEMPRE AO PEDRÃO! ', 'BOM DIA!'))
