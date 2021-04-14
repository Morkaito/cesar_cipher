message = input('Digite a mensagem que deseja descriptografar: ')

LETTERS = 'QAZXSWEDCVFRTGBNHYUJMKILOÇPÁÀÃÂÉÈÊÍÌÎÚÙÛÓÒÔÕ,.;<>:}{][)(-+=*/_!@#$%&?\|'

for key in range(len(LETTERS)):

    translated = ''

    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            num -= key
            if num < 0:
                num += len(LETTERS)
            translated += LETTERS[num]
        else:
            translated += symbol

    print('#KEY {} - {}'.format(key,translated))
