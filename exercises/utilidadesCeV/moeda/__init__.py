def resumo(val, vAum, vDim):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f'{"Preço Analisado:":<20}{moeda(val)}')
    print(f'{"Metade do Preço:":<20}{metade(val, True)}')
    print(f'{"Dobro do Preço:":<20}{dobro(val, True)}')
    print(f'{f"{vAum}% de Aumento:":<20}{aumentar(val, vAum, True)}')
    print(f'{f"{vDim}% de Redução:":<20}{diminuir(val, vDim, True)}')
    print('-' * 30)


def moeda(p0):
    return f'R${p0:.2f}'.replace('.', ',')


def metade(p1, form=False):
    resp = p1 / 2
    return moeda(resp) if form else resp


def dobro(p2, form=False):
    resp = p2 * 2
    return moeda(resp) if form else resp


def aumentar(p3, pAum, form=False):
    resp = p3 + (p3 * pAum / 100)
    return moeda(resp) if form else resp


def diminuir(p4, pDim, form=False):
    resp = p4 - (p4 * pDim / 100)
    return moeda(resp) if form else resp
