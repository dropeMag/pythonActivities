frase = input('Digite uma frase: ').lower().strip()
numA = frase.count('a')
priA = frase.find('a')
ultA = frase.rfind('a')

print("A frase possui {} A's, estando a primeira na {}ª posição e a última na {}ª posição!".format(numA, priA+1, ultA+1))
