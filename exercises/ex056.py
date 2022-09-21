fibo1 = 0
fibo2 = 1
cont = 1

qnt = int(input('Qual a posição deseja saber? '))

if qnt == 1:
    resp = fibo1
elif qnt == 2 or qnt == 3:
    resp = fibo2
else:
    while cont < qnt:
        resp = fibo1 + fibo2

        if cont % 2 == 0:
            fibo1 = resp
        elif cont % 2 != 0:
            fibo2 = resp

        cont += 1

print('A {}ª posição é o número {}'.format(qnt, resp))
