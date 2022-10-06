def leiaDinheiro(msg):
    ok = False
    while not ok:
        dado = str(input(msg)).strip().replace(',', '.')

        if dado.isalpha() or dado == '':
            print(f'[ERRO] "{dado}" não é um preço válido')
        else:
            ok = True
            return float(dado)
