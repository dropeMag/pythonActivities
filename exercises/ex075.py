frase = input('Escreva uma expressão: ')

calc = []

for c in frase:
    if c == '(':
        calc.append(c)
    elif c == ')':
        if frase.index(c) > 0:
            calc.pop()
        else:
            calc.append(c)

if len(calc) == 0:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está errada!')
