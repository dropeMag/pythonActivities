nomeCompleto = input('Informe o seu nome completo: ')
nomeCompleto.strip()

print('\nSeu nome com todas as letras em maiúsculo: {}'.format(nomeCompleto.upper()))
print('Seu nome com todas as letras em minúsculo: {}'.format(nomeCompleto.lower()))
print('Quantas letras o seu nome possui: {}'.format((len(nomeCompleto))-(nomeCompleto.count(' '))))
nomeSeparado = nomeCompleto.split()
print('Quantas letras tem o primeiro nome: {}'.format(len(nomeSeparado[0])))
print("Seu nome tem 'Silva'? {}".format('Silva' in nomeCompleto))
print('Seu primeiro nome: {}'.format(nomeSeparado[0]))
ultimoNome = nomeSeparado[::-1]
print('Seu último nome: {}'.format(ultimoNome[0]))