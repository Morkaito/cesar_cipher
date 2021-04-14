#-*- coding: utf-8 -*-

red = '\033[0;31m'
green = '\033[0;32m'
white = '\033[0;0m'
blue = '\033[0;36m'

mode = input('Deseja '+red+'encrypt'+white+'/'+green+'decrypt'+white+' uma mensagem? ')

message = input('\nInsira a mensagem: ')

key = 13

LETTERS = 'QAZXSWEDCVFRTGBNHYUJMKILOÇPÁÀÃÂÉÈÊÍÌÎÚÙÛÓÒÔÕ,.;<>:}{][)(-+=*/_!@#$%&?\|'

translated = ''

message = message.upper()

print(message)

print('\n['+blue+'*'+white+'] - Iniciado...')

for symbol in message:
    if symbol in LETTERS:
        num = LETTERS.find(symbol)
        if mode == "encrypt":  
            num += key
        elif mode == 'decrypt':
            num -= key

        if num >= len(LETTERS):
            num -= len(LETTERS)
        elif num < 0:
            num += len(LETTERS)

        translated += LETTERS[num]

    else:
        translated += symbol

print("\nResult: ", translated.lower())
