precoNormal = float(input('Qual o valor a ser pago? R$ '))
print('\nFormas de pagamento:')
print('\n[1] Dinheiro/cheque')
print('[2] À vista no cartão')
print('[3] Até 2x no cartão')
print('[4] 3x ou mais no cartão')
formPag = int(input('\nQual a opção desejada? R: '))

if formPag == 1:
    precoPagamento = precoNormal - ((precoNormal * 10) / 100)
elif formPag == 2:
    precoPagamento = precoNormal - ((precoNormal * 5) / 100)
elif formPag == 3:
    precoPagamento = precoNormal
elif formPag == 4:
    precoPagamento = precoNormal + ((precoNormal * 20) / 100)

print('O total a ser pago será de R$ {:.2f}'.format(precoPagamento))
