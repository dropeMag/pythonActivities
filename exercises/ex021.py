cep = input('Digite o nome de uma cidade: ').lower().strip()
santo = 'santo' in cep[:5]

print('O nome da cidade começa com Santo? {}'.format(santo))
