fr1 = input('Escreva uma frase: ').strip().lower()
fr2 = fr1.replace(" ", "")
tamanho = len(fr2)
calc = (tamanho - 1)
rsp = " "

for cont in range(0, tamanho):
    if fr2[cont] != fr2[calc]:
        rsp = " não "
    calc -= 1

print('A sua frase{}é um palíndromo!'.format(rsp))
