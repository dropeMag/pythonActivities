def fatorial(n, s=False):
    f = 1
    for c in range(n, 0, -1):
        if s:
            if c == 1:
                print(c, end=' = ')
            else:
                print(c, end=' * ')
        f *= c
    print(f)


num = int(input('Qual número será fatorado? '))
show = str(input('Você quer o cálculo? [S/N] ')).strip().lower()
print('RESULTADO:')
if show[0] == 's':
    fatorial(num, s=True)
elif show[0] == 'n':
    fatorial(num)
