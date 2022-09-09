frase = input('Digite uma frase: ').lower()
numA = frase.count('a')
priA = frase.find('a')
ultA = frase[::-1].find('a')

print("A frase possui {} a's, estando a primeira na {}ª posição e a última na {}ª posição!".format(numA, priA+1, ultA+1))
