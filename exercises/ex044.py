num = int(input('De qual número você quer a tabuada? \nR: '))

for cont in range(1, 11):
    print('{:02} x {} = {}'.format(cont, num, (cont*num)))
