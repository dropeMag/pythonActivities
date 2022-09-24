from random import randint
compt = randint(1, 2)
vitorias = 0

print('-=' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=' * 15)

while True:
    userOpc = input('Par ou Ímpar? [P/I] ').upper()
    userNum = int(input('Diga um valor: '))

    if userOpc == 'I':
        if (compt + userNum) % 2 == 0:
            break
        else:
            print('Você venceu! Vamos novamente!')
            vitorias += 1
    elif userOpc == 'P':
        if (compt + userNum) % 2 != 0:
            break
        else:
            print('Você venceu! Vamos novamente!')
            vitorias += 1
    else:
        print('Valor inválido! Responda novamente!')

print('_' * 30)
print('FIM DE JOGO!')
print(f'Voce venceu {vitorias} vez(es)!')
