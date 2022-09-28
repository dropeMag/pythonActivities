print('{:-^40}\n{: ^40}\n{:-^40}'.format('', ' LOJA DO PEDRÃO ', ''))
acimaMil = total = precoBarato = 0
produBarato = ' '

while True:
    produto = input('Nome do Produto: ')
    preco = float(input(f'Preço do {produto}: R$ '))

    while preco < 0:
        print('Preço Inválido!')
        preco = float(input(f'Preço do {produto}: R$ '))

    if preco > 1000:
        acimaMil += 1

    if total == 0 or preco < precoBarato:
        precoBarato = preco
        produBarato = produto

    total += preco

    contin = input('Deseja Continuar? [S/N] ').strip()

    while contin not in 'SsNn':
        contin = input('Deseja Continuar? [S/N] ')

    if contin in 'Nn':
        break

print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R$ {total:.2f}')
print(f'Temos {acimaMil} produto(s) acima de R$ 1000,00')
print(f'O produto mais barato foi {produBarato}, que custa R$ {precoBarato:.2f} ')
