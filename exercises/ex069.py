palavras = 'aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro'

for cnt1 in palavras:
    print(f'Na palavra {cnt1.upper()} temos as vogais: ', end='')

    for cnt2 in cnt1:
        if cnt2 in 'aeiou':
            print(cnt2, end=' ')

    print('')
