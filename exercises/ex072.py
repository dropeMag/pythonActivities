valores = []

for v in range(0, 5):
    num = int(input('Digite um número: '))

    for c in range(0, len(valores)):
        if valores[c] > num or valores[c] == num and v != 0:
            valores.insert(c, num)
            print(f'{num} adicionado na posição {c} da lista.')
            break
        elif max(valores) < num or v == 0:
            valores.append(num)
            print(f'{num} adicionado no final da lista.')
            break

print(f'Os valores informados, em ordem, foram: {valores}')
