resp = soma = qnt = 0

while resp != 999:
    resp = int(input('Informe um valor: '))

    if qnt == 0:
        menNum = maiNum = resp

    soma += resp
    qnt += 1

    if resp != 999:
        if resp > maiNum:
            maiNum = resp

        if resp < menNum:
            menNum = resp

print('Foram informados {} números'.format(qnt-1))
print('A soma é de {}'.format(soma-999))
print('A média é de {}'.format((soma-999)/(qnt-1)))
print('O menor número foi: {}'.format(menNum))
print('O maior número foi: {}'.format(maiNum))
