valores = []

for c1 in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {c1}: ')))

print(f'O menor valor foi {min(valores)}, nas posições:', end=' ')
for c2 in range(0, len(valores)):
    if valores[c2] == min(valores):
        print(c2, end='... ')

print('')

print(f'O maior valor foi {max(valores)}, nas posições:', end=' ')
for c2 in range(0, len(valores)):
    if valores[c2] == max(valores):
        print(c2, end='... ')
