from utilidadesCeV import moeda, dado

preco = dado.leiaDinheiro(('Informe o preço: R$ '))
#aumentar = dado.leiaDinheiro(str(input('Quantos % deseja aumentar? ')))
#diminuir = dado.leiaDinheiro(str(input('Quantos % deseja diminuir? ')))
moeda.resumo(preco, 80, 30)
