def escreva(txt):
    tmn = len(txt) + 2
    print('~' * tmn)
    print(f' {txt}')
    print('~' * tmn)


texto = str(input('Escreva um texto: '))
escreva(texto)
