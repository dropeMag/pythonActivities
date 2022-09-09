r1 = float(input('Informe o valor da 1ª reta: '))
retaMaior = r1

r2 = float(input('Informe o valor da 2ª reta: '))
if r2 > retaMaior:
    retaMaior = r2

r3 = float(input('Informe o valor da 3ª reta: '))
if r3 > retaMaior:
    retaMaior = r3

retaSoma = (r1+r2+r3)-retaMaior
if retaSoma<=retaMaior:
    print('As retas não podem formar um triângulo!')
else:
    print('As retas podem formar um triângulo!')
