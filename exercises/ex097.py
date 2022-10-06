def ajuda(msg):
    print('~' * 75)
    print(f'{f"MANUAL DO COMANDO {cmd.upper()}":^75}')
    print('~' * 75)
    help(msg)


while True:
    print('-' * 75)
    cmd = str(input('Biblioteca ou Comando: ')).lower()

    if cmd == 'fim':
        break

    ajuda(cmd)


print('=' * 75)
print(f'{"ATÉ LOGO":^75}')
print('=' * 75)
