listagem = 'Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.9
cnt = 0

print('-'*40)
print('{: ^40}'.format('LISTAGEM DE PREÇOS'))
print('-'*40)

while cnt < len(listagem):
    print('{:.<31}'.format(listagem[cnt]), end='')
    cnt += 1
    print('R$ {: >6.2f}'.format(listagem[cnt]))
    cnt += 1

print('-'*40)
